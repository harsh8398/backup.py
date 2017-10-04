import shutil
import os


class Backup(object):
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst

    def do_only_copy(self, file_list):
        """copies the list of files from source to destination"""
        data = ""
        for f in file_list:
            abs_dst = f.replace(self.src, self.dst, 1)
            abs_dst = os.sep.join((abs_dst.split(os.sep))[:-1])
            shutil.copy(f, abs_dst)
            data += str("Copied: " + str(f) + " -> "
                        + f.replace(self.src, self.dst) + "\n")
        return (data)
