__author__ = 'xaled'

import judo.profile
import judo.run
from judo.config import RG_PROFILE
#import judo.frequent
#import frequentree.os
import logging
import sys

"""
judo: jailed user do (like sudo but sandbox execution instead)

USAGE: #TODO
judo  [-u] profile command"
-u: update profile

Example:  $ judo clean firefox
"""

logging.config.fileConfig("logging.conf")
logger = logging.getLogger(__name__)
logger.debug('often makes a very good meal of %s', 'visiting tourists')
print "test"


# CONST
DEFAULT_CMD = ""
DEFAULT_PFL = ""

def Main(cmd=DEFAULT_CMD, profile=DEFAULT_PFL, update=False): #other options
    prfl=judo.profile.getProfile(profile)
    rn = judo.run.Run(prfl)
    rn.init()
    rn.execute()
    rn.clean()


if __name__ == "__main__":
    #initJU() #TODO: initJUDO & installJUDO scripts (cleaning unvalid locks)
    if len(sys.argv) <3 or (sys.argv[1]=='-u' and len(sys.argv)< 4):
        print "usage: judo  [-u] profile command"
    else:
        start = 0
        update = False
        if sys.argv[1]=='-u':
            start = 1
            update = True
        profile = sys.argv[1+start]
        cmd= ""
        for a in sys.argv[2+start:]:
            cmd += a + " "
        if not RG_PROFILE.match(profile):
            print "Profile name should be alphanumerical and less than 20 characters"
        else:
            Main(cmd=cmd,profilename=profile,update=update)


