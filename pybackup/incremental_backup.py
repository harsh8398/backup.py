import os
import shutil
from .backup import Backup


class IncrementalBackup(Backup):
    def __init__(self, src, dst):
        super().__init__(src, dst)
        self.THRESHOLD_DIFF_RATIO = 0.75
        self.WHOLE_COPY_CONST = 0
        self.PARTIAL_COPY_CONST = 1

    @staticmethod
    def scantree(path):
        for entry in os.scandir(path):
            if entry.is_dir(follow_symlinks=False):
                yield from IncrementalBackup.scantree(entry.path)
            else:
                yield entry

    def _get_dst_path_from_src(self, path):
        return str.replace(path, self.src, self.dst, 1)

    def _get_diff_files(self):
        src_entries = self._scantree(self.src)
        for entry in src_entries:
            if not os.path.exists(self._get_dst_path_from_src(entry.path)):
                yield entry.path, self.WHOLE_COPY_CONST
            elif entry.stat.st_mtime >= self._metadata["last_run_epoch"]:
                yield entry.path, self.PARTIAL_COPY_CONST

    @staticmethod
    def patch_file(self, src_file, dst_file):
        # unpatched = open(dst_file, "rb")
        # hashes = pyrsync.blockchecksums(unpatched)
        # patchedfile = open(src_file, "rb")
        # delta = pyrsync.rsyncdelta(patchedfile, hashes)
        # unpatched.seek(0)
        # save_to = open(dst_file, "wb")
        # pyrsync.patchstream(unpatched, save_to, delta)
        pass

    @staticmethod
    def copy_file(src_file, dst_file):
        shutil.copy2(src_file, dst_file)

    def _copytree(self):
        diff_files = self._get_diff_files()
        for filepath, action in diff_files:
            src_filepath = filepath
            dst_filepath = self._get_dst_path_from_src(filepath)
            if action == self.WHOLE_COPY_CONST:
                # XXX: should we preserve metadata?
                self.copy_file(src_filepath, dst_filepath)
            elif action == self.PARTIAL_COPY_CONST:
                self.patch_file(src_filepath, dst_filepath)

    def run(self):
        if not os.path.exists(self.dst):
            os.makedirs(self.dst)
        self._copytree()
