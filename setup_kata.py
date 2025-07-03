#!/usr/bin/env python3
import os
import shutil
import subprocess
from pathlib import Path
import argparse


def init_venv(path: Path) -> None:
    """
    Create and initialize a virtual environment, then install requirements.

    Args:
        path: Path to the project directory
    """
    print("Setting up virtual environment...")
    venv_path = path / '.venv'

    # Create virtual environment
    subprocess.run(['python', '-m', 'venv', '.venv'], cwd=path, check=True)

    # Determine the pip path based on the operating system
    pip_path = venv_path / ('Scripts' if os.name == 'nt' else 'bin') / 'pip'
    print(f"using pip_path {pip_path}")

    # Install requirements if requirements.txt exists
    requirements_file = path / 'requirements.txt'
    if requirements_file.exists():
        print("Installing requirements...")
        subprocess.run(['pip', 'install', '-r', 'requirements.txt'], cwd=path, check=True)
        print("Requirements installed successfully")
    else:
        print("No requirements.txt found, skipping package installation")


def init_git_repo(path: Path) -> None:
    """
    Initialize a git repository, add all files, and create initial commit.

    Args:
        path: Path to the directory to initialize
    """
    print("Initializing git repository...")
    subprocess.run(['git', 'init'], cwd=path, check=True)
    subprocess.run(['git', 'add', '.'], cwd=path, check=True)
    subprocess.run(['git', 'commit', '-m', 'initial import'], cwd=path, check=True)
    print("Git repository initialized with initial commit")


def list_katas() -> None:
    """
    List all available katas by checking the contents of _kata_descriptions directory.
    """
    try:
        # Clone the website repository if it doesn't exist
        clone_repository('https://github.com/sammancoaching/website.git', 'sammancoaching.org')

        kata_desc_path = Path('sammancoaching.org/_kata_descriptions')
        if not kata_desc_path.exists():
            print("Error: Kata descriptions directory not found")
            return

        print("\nAvailable katas:")
        for file_path in sorted(kata_desc_path.glob('*.md')):
            kata_name = file_path.stem  # Get filename without extension
            print(f"  {kata_name}")

    except Exception as e:
        print(f"Error listing katas: {e}")


def clone_repository(url: str, target_dir: str) -> None:
    """
    Clone a git repository to the specified directory if it doesn't exist.
    If the repository already exists, update it with git pull.

    Args:
        url: Repository URL
        target_dir: Target directory for cloning
    """
    target_path = Path(target_dir)
    if target_path.exists():
        print(f"Repository exists in {target_dir}, updating...")
        try:
            subprocess.run(['git', 'pull'], cwd=target_dir, check=True)
            print(f"Successfully updated {target_dir}")
        except subprocess.CalledProcessError as e:
            print(f"Error updating repository: {e}")
    else:
        print(f"Cloning {url} into {target_dir}...")
        subprocess.run(['git', 'clone', url, target_dir], check=True)


def setup_kata(kata_name: str) -> None:
    """
    Set up a new kata environment by cloning necessary repositories
    and copying template files.

    Args:
        kata_name: Name of the kata to set up
    """
    current_dir = Path.cwd()

    try:
        # Clone repositories
        clone_repository('https://github.com/sammancoaching/website.git', 'sammancoaching.org')
        clone_repository('https://github.com/emilybache/starter.git', 'starter')

        # Check for kata description file first
        kata_desc_file = Path(f'sammancoaching.org/_kata_descriptions/{kata_name}.md')
        if not kata_desc_file.exists():
            print(f"Error: Kata description file not found: {kata_desc_file}")
            return

        print(f"Found kata description: {kata_desc_file}")

        # Copy the Python starter code
        source_path = Path('starter/python')
        target_path = Path(kata_name)
        print(f"Copying Python starter code to {kata_name}...")
        shutil.copytree(source_path, target_path)

        # Copy the kata description file as README.md
        shutil.copy2(kata_desc_file, target_path / 'README.md')
        print(f"Copied kata description to {target_path}/README.md")

        init_git_repo(target_path)

        init_venv(target_path)

    except subprocess.CalledProcessError as e:
        print(f"Error during git operation: {e}")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    finally:
        # Return to original directory
        os.chdir(current_dir)


def main():
    parser = argparse.ArgumentParser(
        description="Set up a new kata environment with necessary repositories and starter code"
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--list", help="List all available katas", action="store_true")
    group.add_argument("kata_name", help="Name of the kata to set up", nargs='?')


    args = parser.parse_args()

    if args.list:
        list_katas()
    elif args.kata_name:
        setup_kata(args.kata_name)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()