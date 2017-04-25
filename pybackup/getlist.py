import os


class GetList(object):
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst

    def flist(self):
        """returns list of files that are available in source but not
        in destination and files that are modified"""
        mylist = []
        sonlyfiles = []
        donlyfiles = []
        for path, subdirs, files in os.walk(self.dst):
            for name in files:
                donlyfiles.append(os.path.join(path, name))
        for path, subdirs, files in os.walk(self.src):
            for name in files:
                sonlyfiles.append(os.path.join(path, name))
        for sourcef in sonlyfiles:
            destf = sourcef.replace(self.src, self.dst, 1)
            if destf in donlyfiles:
                t1 = os.path.getmtime(sourcef)
                t2 = os.path.getmtime(destf)
                if t2 > t1:
                    pass
                else:
                    mylist.append(sourcef)
            else:
                mylist.append(sourcef)
        return (mylist)
