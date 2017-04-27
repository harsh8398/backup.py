import shutil
import os


class BckpList(object):
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst

    def doCopy(self, mylist):
        """copies the list of files from source to destination"""
        data = ""
        for f in mylist:
            absDst = f.replace(self.src, self.dst, 1)
            absDst = os.sep.join((absDst.split(os.sep))[:-1])
            shutil.copy(f, absDst)
            print(f.replace(self.src, self.dst))
            data += str("~ Copied -> " + str(f) + "\n")
        return (data)
