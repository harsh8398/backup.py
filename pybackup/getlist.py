import os


class GetList(object):
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst

    def flist(self):
        """returns list of files that are available in source but not
        in destination"""
        mylist = []
        onlyfiles = []
        onlyname = []
        for path, subdirs, files in os.walk(self.dst):
            for name in files:
                onlyfiles.append(os.path.join(path, name))
                onlyname.append(name)
        for path, subdirs, files in os.walk(self.src):
            for name in files:
                if name in onlyname:
                    pass
                else:
                    mylist.append(os.path.join(path, name))
        return (mylist)
