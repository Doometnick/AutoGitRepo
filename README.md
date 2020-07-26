# AutoGitRepo

Creates a local repository and connects it go https://www.github.com/ without any manual effort.

A batch script creates the project folder, initializes a git repository, adds a README.md, and a python script logs on to github, creates a remote repository and connects it with the local one.

## Setup
The ``gitproject.bat`` file has to be put in a folder that exists in your PATH variable, so that it can be called from anywhere in the command line prompt.

A ``.env`` file is required that contains your username and password for your github login. Do not make this information public! An example file ``.env_example`` is attached.

Change the following four variables in the gitproject.bat file according to your preferences/folder structures:
- _BASE_FOLDER_: This is where all new created Github repositories will be placed in by the script.
- _GIT_CONNECT_SCRIPT_: Location of the python script ``github_connect.py`` (should be in the same folder).
- _GITHUB_USER_DOMAIN_: Link to your personal Github.
- _PYTHON_EXE_: Path to your python installation so that command line can run python scripts.
