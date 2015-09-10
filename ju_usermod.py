#!/usr/bin/python
__author__ = 'xaled'
import sys
import os
import re

GP_RE = "^[a-z][a-z0-9]+(,[a-z][a-z0-9]+)*$"

def checkGroupVector(groupv):
    if len(groupv) > 200:
        return False
    if re.match(GP_RE,groupv):
        return True
    return False

if __name__ == "__main__":
    if len(sys.argv)<3:
        print "ju_usermod needs two arguments: uid and group vector"
        sys.exit(1)
    uid = int(sys.argv[1])
    if uid <8800 or uid > 8900:
        print "uid not valid"
        sys.exit(2)
    if not checkGroupVector(sys.argv[2]):
        print "group vector not valid"
        sys.exit(3)
    cmd = "/usr/sbin/usermod -a -G %s ju%d"%(sys.argv[2],uid)
    print cmd
    os.system(cmd)
