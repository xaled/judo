#!/usr/bin/python
__author__ = 'xaled'
import sys
import os
import re

PREFIX = "/tmp/judo_temphomes/ju_"
LP = len(PREFIX)
RE_WP = "^[a-z][a-z0-9]+\\.\\d{4}\\.\\d{1,10}$"
MAX_LEN = 100

def checkWorkPath(wp):
    #/tmp/judo_temphomes/ju_tpoidefault.8892.23809
    if len(wp) > MAX_LEN:
        return False
    if not PREFIX == wp[:LP]:
        return False
    # Regex
    if re.match(RE_WP,wp[LP:]):
        return True
    return False


if __name__=="__main__":
    if len(sys.argv)<3:
        print "ju_useradd needs two arguments: uid and workpath"
        sys.exit(1)
    uid = int(sys.argv[1])
    if uid <8800 or uid > 8900:
        print "uid not valid"
        sys.exit(2)
    if not checkWorkPath(sys.argv[2]):
        print "workpath not valid"
        sys.exit(3)
    cmd = "/usr/bin/useradd -u %d -d '%s' -M ju%d"%(uid,sys.argv[2],uid)
    print cmd
    os.system(cmd)