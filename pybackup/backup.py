import os
import shutil
import json
import time

from .errors import InvalidMetadataError

# Descriptor attribute for a path type-checked attribute
# TODO: Maybe replace with pathlib?
class Path:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError("Expected a str")
        value = os.path.abspath(value)
        if not os.path.exists(value):
            raise ValueError("Expected a valid existing path string")
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class Backup(object):
    src = Path('src')
    dst = Path('dst')
    def __init__(self, src, dst):
        self.src = src
        self.dst = src
        if self.src == self.dst:
            raise ValueError("Source and destination paths can not be the same")
        # TODO: give support for skipping dot files & dirs
        # TODO: give follow symlink support
        self.METADATA_DIR = os.path.join(self.src, ".pybackup")
        self._get_metadata()

    def _get_metadata(self):
        try:
            with open(os.path.join(self.src, ".pybackup/metadata.json"), "r") as f:
                data = json.load(f)
            self._metadata = data["last_run_epoch"]
        except FileNotFoundError:
            self._metadata = {"last_run_epoch": 0}
        except KeyError:
            raise InvalidMetadataError("Metadata seems to be tampered!")

    def _save_metadata(self):
        if not os.path.exists(self.METADATA_DIR):
            os.mkdir(self.METADATA_DIR)
        with open(os.path.join(self.src, ".pybackup/metadata.json"), "w") as f:
            json.dump(self._metadata, f, indent=2)

    def _scantree(self, path):
        for entry in os.scandir(path):
            if entry.is_dir(follow_symlinks=False):
                yield from self._scantree(entry.path)
            else:
                yield entry

    def run(self):
        # TODO: give some warning when there already exists files in dst dir
        # this class on its own does full backup
        # https://stackoverflow.com/questions/22078621/python-how-to-copy-files-fast
        shutil.copytree(self.src, self.dst)
        self._metadata["last_run_epoch"] = time.time()
        # TODO: maybe check every file in dst to ensure we are saving correct epoch time?
        self._save_metadata()
