import pytest
from pybackup import Backup

def test_backup(tmpdir):
    testsrc = tmpdir.mkdir("src")
    testsrc.join("hello.txt").write("content")
    testdst = tmpdir.mkdir("dst")
    Backup(src=testsrc.absolute(), dst=testdst.absolute()).run()