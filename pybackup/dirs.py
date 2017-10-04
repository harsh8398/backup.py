import os


class Dirs(object):
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst

    def ensure_dir(self, file_path):
        """Ensures if given path is available directory or not
        if it is then pass else create directory"""
        directory = os.path.dirname(file_path)
        if not os.path.exists(directory):
            os.makedirs(directory)

    def make_dirs(self, mylist):
        """creates directories that are available in source but not
        in destination"""
        for file_path in mylist:
            abs_dst = file_path.replace(self.src, self.dst)
            self.ensure_dir(abs_dst)
        return True
