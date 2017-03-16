from nose.tools import *
import pybackup


def test_getlist():
    obj = pybackup.GetList('/home/harsh8398/Desktop/d1',
                           '/home/harsh8398/Desktop/d2')
    assert_equal(obj.src, '/home/harsh8398/Desktop/d1')
    assert_equal(obj.dst, '/home/harsh8398/Desktop/d2')
    assert_equal(obj.flist(), ['/home/harsh8398/Desktop/d1/Untitled Document'])


def test_bckplist():
    obj = pybackup.GetList('/home/harsh8398/Desktop/d1',
                           '/home/harsh8398/Desktop/d2')
    mylist = obj.flist()
    obj1 = pybackup.BckpList(obj.src, obj.dst)
    assert_equal(obj1.src, '/home/harsh8398/Desktop/d1')
    assert_equal(obj1.dst, '/home/harsh8398/Desktop/d2')
    assert_equal(
        obj1.docopy(mylist),
        '~ Copied -> /home/harsh8398/Desktop/d1/Untitled Document\n')
