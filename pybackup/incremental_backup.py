import os
import difflib
from io import BytesIO
from .backup import Backup


class IncrementalBackup(Backup):
    def __init__(self, src, dst):
        super().__init__(src, dst)
        # TODO: use this to incrementaly copy bytes of files
        self.THRESHOLD_FILE_BYTES = 1024
        self.THRESHOLD_DIFF_RATIO = 0.75

    def _files(self, dirpath):
        for dirname, _, filenames in os.walk(dirpath):
            for filename in filenames:
                yield os.path.join(dirname, filename)
    
    def _get_diff_files(self):
        # TODO: get list of all files which are modified after `last_run_epoch`

        src_files = self._files(self.src)
        for file in src_files:
            if os.path.getmtime(file) >= self._metadata["last_run_epoch"]:
                yield file
    
    def _get_diff_file_bytes_range(self):
        # TODO: return tuple list of file's different bytes pos range
        pass

    def _copy_file_bytes(self, file, opcodes):
        # TODO: user `os.copy_file_range` for better performance
        for tag, i1, i2, j1, j2 in opcodes:
            pass
            
    def _copy_files(self, files):
        for f in files:
            src_file = f
            dst_file = f.replace(self.src, self.dst, 1)
            # with open(src_file, "rb") as src_fin, open(dst_file, "rb") as dst_fin:
            #     diff = difflib.diff_bytes(None, src_fin, dst_fin)

    def run(self):
        files = self._get_diff_files()
        self._copy_files(files)
