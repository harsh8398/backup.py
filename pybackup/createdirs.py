import os


class CreateDirs(object):
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst

    def ensureDir(self, file_path):
        directory = os.path.dirname(file_path)
        if not os.path.exists(directory):
            os.makedirs(directory)

    def makeDirs(self, mylist):
        """creates directories that are available in source but not
        in destination"""
        for file_path in mylist:
            absDst = file_path.replace(self.src, self.dst)
            self.ensureDir(absDst)
        return True
