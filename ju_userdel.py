#!/usr/bin/python
__author__ = 'xaled'
import sys
import os

if __name__ == "__main__":
    if len(sys.argv)<2:
        print "ju_userdel needs one arguments: uid"
        sys.exit(1)
    uid = int(sys.argv[1])
    if uid <8800 or uid > 8900:
        print "uid not valid"
        sys.exit(2)
    cmd = "/usr/bin/pkill -9 -u ju%d"%(uid)
    print cmd
    os.system(cmd)
    cmd = "/usr/sbin/userdel ju%d"%(uid)
    print cmd
    os.system(cmd)


