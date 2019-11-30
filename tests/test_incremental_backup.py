import pytest
import json
from pybackup import IncrementalBackup


def test_copy(tmpdir):
    testdst = tmpdir.mkdir("dst")
    testdst.join("hello.txt").write("old content")
    testsrc = tmpdir.mkdir("src")
    testsrc.join("hello.txt").write("content")
    IncrementalBackup(src=testsrc.strpath, dst=testdst.strpath).run()
    assert testdst.join("hello.txt").read() == "content"