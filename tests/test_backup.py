import pytest
import json
from backup import Backup

def test_copy(tmpdir):
    testsrc = tmpdir.mkdir("src")
    testsrc.join("hello.txt").write("content")
    # testdst = tmpdir.mkdir("dst")
    Backup(src=testsrc.strpath, dst=tmpdir.join("dst/").strpath).run()
    assert tmpdir.join("dst/hello.txt").read() == "content"

def test_metadata(tmpdir):
    testsrc = tmpdir.mkdir("src")
    testsrc.join("hello.txt").write("content")
    # testdst = tmpdir.mkdir("dst")
    obj = Backup(src=testsrc.strpath, dst=tmpdir.join("dst/").strpath)
    obj.run()
    metadata = json.load(testsrc.join(".pybackup/metadata.json"))
    assert obj._metadata["last_run_epoch"] == metadata["last_run_epoch"]