# PYBACKUP

Recursive/Incremental Backup Using Python

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You need to install Python 3.5 or above on your machine and pip for python for installing the project on your machine.

```
For installing Python go to https://www.python.org and for installing pip, Download get-pip.py from https://https://bootstrap.pypa.io/get-pip.py to a folder on your computer. Open a command prompt window and navigate to the folder containing get-pip.py. Then run python get-pip.py in your Command Prompt/Terminal(Windows/Linux). This will install pip.
```

### Installation

Downloading the project from git

```
You can download this project by clicking the button clone or download at the top of the repository.
```

Step 1:

```
Download and Extract the project files.
```

Step 2:

```
Open up your Terminal and change your current working directory to project directory that is path/to/pybackup.Make sure you are in the direcotry pybackup that has file setup.py in it.
```

Final Step:

```
Run the command 'pip install .' without the quotation.
```

## Running the tests

You can run included test script by typing command 'nosetests' in project directory.But you need to install nose package first.

### Start using script for your daily backup

You can start using this script for you personal use...

```
After installation you can run 'pybackup path/to/source/directory path/to/destination/directory' in Terminal to backup your file to destination directory or sync destination directory with source directory.
```

## Versioning

For the versions available, see the [tags on this repository](https://github.com/harsh8398/pybackup/tags).

## Authors

* **Harsh Patel** - *Initial work* - [harsh8398](https://github.com/harsh8398)

See also the list of [contributors](https://github.com/harsh8398/pybackup/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* inspired by rsync
