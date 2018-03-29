import pybackup
import os
src = '.' + os.sep + 'src' + os.sep
dst = '.' + os.sep + 'dst' + os.sep


def test_blank():
    if not os.path.exists(src):
        os.makedirs(src)
    if not os.path.exists(dst):
        os.makedirs(dst)
    Files = pybackup.Files(src, dst)
    flist = Files.get_files()
    assert len(flist) == 0
    Dirs = pybackup.Dirs(src, dst)
    assert Dirs.make_dirs(flist) == True
    if os.path.exists(src):
        os.rmdir(src)
    if os.path.exists(dst):
        os.rmdir(dst)
