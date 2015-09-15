__author__ = 'xaled'

import judo.profile
import judo.run
#import judo.frequent
#import frequentree.os

# CONST
DEFAULT_CMD = ""
DEFAULT_PFL = ""

def Main(cmd=DEFAULT_CMD, profile=DEFAULT_PFL, update=False): #other options
    prfl=judo.profile.getProfile(profile)
    #TODO: check profile if doesn't exist prompt question to create or not?
    rn = judo.run.Run(prfl)
    rn.init()
    rn.execute() # TODO: blocking or not blocking exec!
    #TODO: check if there are still other process belonging to jailed uid
    #TODO: check if execution has exited
    rn.clean()

