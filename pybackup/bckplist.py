import shutil
import os


class BckpList(object):
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst

    def docopy(self, mylist):
        """copies the list of files from source to destination"""
        data = ""
        for f in mylist:
            absDst = f.replace(self.src, self.dst, 1)
            absDst = "/".join((absDst.split("/"))[:-1])
            shutil.copy(f, absDst)
            print(f.replace(self.src, self.dst))
            data += str("~ Copied -> " + str(f) + "\n")
        return (data)
