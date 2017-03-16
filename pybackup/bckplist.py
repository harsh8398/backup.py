import shutil
from os.path import abspath


class BckpList(object):
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst

    def docopy(self, mylist):
        """copies the list of files from source to destination"""
        data = ""
        for f in mylist:
            shutil.copy(f, self.dst)
            data += str("~ Copied -> " + str(f) + "\n")
        return (data)
