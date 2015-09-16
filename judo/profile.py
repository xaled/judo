__author__ = 'xaled'
from os.path import isdir, isfile, join
from config import DEFAULT_PROFILE_CONF, RG_PROFILE,DEFAULT_PROFILE_DIR
import json
import logging


logger = logging.getLogger(__name__)





def getProfiles(profiledir=DEFAULT_PROFILE_DIR): # TODO: Get all Available profiles:
    """
    Get all available profiles in a profiledir
    """
    pass


def createProfile(profilename):
    profile = getProfile(profilename)
    if profile == None:
        profile = createProfile(profilename)

    return profile



def getProfile(profilename,profiledir=DEFAULT_PROFILE_DIR):
    if not RG_PROFILE.match(profilename):
        raise ProfilaException("Profile name should be alphanumerical and less than 20 characters",None)
    profile_conf_file = join(profiledir, profilename + ".json")
    profile_dir = join(profiledir,profilename)
    if isfile(profile_conf_file) and isdir(profile_dir):
        try:
            fin = open(profile_conf_file,"r")
            data = fin.read()
            conf = json.loads(data)
            fin.close()
            return conf,profile_dir
        except Exception, e:
            raise ProfilaException("Error loading profile conf file: " + profile_conf_file,e)
    logger.info("Profile not found; profilename=%s", profilename)
    return None

class Profile:
    profilename = ""
    profiledir  = ""
    profileconf = None
    def __init__(self):
        pass



class ProfilaException(Exception):
    def __init__(self, message, cause):
        super(ProfilaException, self).__init__(message + ', caused by ' + repr(cause))
        self.cause = cause

