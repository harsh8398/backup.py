from os import listdir
from os.path import isfile, join, realpath


class GetList(object):
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst

    def flist(self):
        """returns list of files that are available in source but not
        in destination"""
        mylist = []
        onlyfiles = [
            f for f in listdir(self.src) if isfile(join(self.src, f))
        ]
        for i in onlyfiles:
            if i in listdir(self.dst):
                pass
            else:
                mylist.append(realpath(i))
        return mylist
