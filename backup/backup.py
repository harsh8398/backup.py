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
        instance.__dict__[self.name] = os.path.abspath(value)

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class Backup(object):
    src = Path("src")
    dst = Path("dst")

    def __init__(self, src, dst):
        self.src = src
        self.dst = dst
        if self.src == self.dst:
            raise ValueError("Source and destination paths can not be the same")
        # TODO: give support for skipping dot files & dirs
        # TODO: give follow symlink support
        # TODO: give support for passing pathlike(https://docs.python.org/3/glossary.html#term-path-like-object) object as src and dst
        self.METADATA_DIR = os.path.join(self.src, ".pybackup")
        self._get_metadata()
        self.YES_VALUES = ["y", "Yes", "1", "true"]

    def _is_yes(self, flag):
        flag = str(flag)
        return True if flag.lower() in self.YES_VALUES else False

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

    def run(self):
        # TODO: give some warning when there already exists files in dst dir
        # this class on its own does full backup
        # https://stackoverflow.com/questions/22078621/python-how-to-copy-files-fast
        if os.path.exists(self.dst):
            print(
                "Warning: Destination dir already exists. Going further will remove the destination dir and its content."
            )
            cont_flag = input("Do you want to continue?(y/N)")
            if self._is_yes(cont_flag):
                shutil.rmtree(self.dst)
            else:
                exit(0)
        shutil.copytree(self.src, self.dst)
        self._metadata["last_run_epoch"] = time.time()
        # XXX: maybe check every file in dst to ensure we are saving correct epoch time? need to make it robust
        self._save_metadata()
