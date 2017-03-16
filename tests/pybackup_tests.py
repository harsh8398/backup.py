from nose.tools import *
import os
import pybackup
src = '/home/harsh8398/Desktop/d1'
dst = '/home/harsh8398/Desktop/d2'


def test_getlist():
    os.mkdir(src)
    os.mkdir(dst)
    f = open(os.path.join(src, 'test.txt'), 'w')
    f.write("this is working")
    f.close()
    obj = pybackup.GetList(src, dst)
    assert_equal(obj.src, src)
    assert_equal(obj.dst, dst)
    assert_equal(obj.flist(), ['/home/harsh8398/Desktop/d1/test.txt'])
    os.remove(os.path.join(src, 'test.txt'))
    os.rmdir(src)
    os.rmdir(dst)


def test_bckplist():
    os.mkdir(src)
    os.mkdir(dst)
    f = open(os.path.join(src, 'test.txt'), 'w')
    f.write("this is working")
    f.close()
    obj = pybackup.GetList(src, dst)
    mylist = obj.flist()
    obj1 = pybackup.BckpList(src, dst)
    assert_equal(obj1.src, src)
    assert_equal(obj1.dst, dst)
    assert_equal(
        obj1.docopy(mylist),
        '~ Copied -> /home/harsh8398/Desktop/d1/test.txt\n')
    f = open(os.path.join(dst, 'test.txt'), 'r')
    assert_equal(f.readline().strip(), 'this is working')
    os.remove(os.path.join(src, 'test.txt'))
    os.remove(os.path.join(dst, 'test.txt'))
    os.rmdir(src)
    os.rmdir(dst)
