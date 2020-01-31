[![Build Status](https://travis-ci.org/harsh8398/pybackup.svg?branch=master)](https://travis-ci.org/harsh8398/pybackup)
[![codecov](https://codecov.io/gh/harsh8398/pybackup/branch/master/graph/badge.svg)](https://codecov.io/gh/harsh8398/pybackup/branch/master)
# PYBACKUP

PyBackup is a recursive/incremental backup utility package written purely in Python. This main feature of the package is its incremental backup which incrementally copies only the files that are added or the parts of the file which are changed. To achieve the later scenario it uses rsync algorithm for which you can find the details [here](https://rsync.samba.org/tech_report/tech_report.html).

### Prerequisites

- Python 3.5 or above

### Quick Install

```sh
pip install git+https://github.com/harsh8398/backup.py.git
```

### Simple Example

This package also installs a script which you can run in the shell as follows:

```sh
pybackup ~/path/to/the/source/dir ~/path/to/the/destination/dir
```

Or you can use its Python interface as follows:

```python
from backup import IncrementalBackup

source_dir = "~/path/to/the/source/dir"
destination_dir = "~/path/to/the/destination/dir"
IncrementalBackup(src=source_dir, dst=destination_dir).run()
```

## Versioning

For the versions available, see the [tags on this repository](https://github.com/harsh8398/pybackup/tags).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.txt) file for details.

## Acknowledgments

This project was solely inspired by [rsync](https://linux.die.net/man/1/rsync).
