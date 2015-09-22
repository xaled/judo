__author__ = 'xaled'
from os.path import isdir, isfile, join
from config import DEFAULT_PROFILE_CONF, RG_PROFILE,DEFAULT_PROFILE_DIR
from frequentree.io import mkdirIfNotExist
import json
import logging

logger = logging.getLogger(__name__)

"""
contains Porfile class and static operations on Porfile
static functions:
- getProfiles()
- createProfile(profilename, template=DEFAULT_TEMPLATE)
- getProfile(profilename)
- getAllProfiles()

classes:
- Profile
- ProfileException

"""



def getAllProfiles(): # TODO: Get all Available profiles:
    """
    Get all available profiles in a profiledir
        :return: - list<Profiles>
        :raises: ProfileException in case of io error
    """
    pass

def saveProfile(profile_conf, profile_conf_file):
    """
    Save profile config to json file
    :param profile_conf: profile config
    :param profile_conf_file: otuput json file
    :raises: IOError
    """
    fou = open(profile_conf_file,"w")
    fou.write(json.dumps(profile_conf,indent=3))
    fou.close()

def createProfile(profilename, profile_template=DEFAULT_PROFILE_CONF):
    """

    :param profilename:
    :param profile_template: template conf, defalt: judo.config.DEFAULT_PROFILE_CONF
    :except:?
    :raises:?
    """
    profile_home = join(DEFAULT_PROFILE_DIR, profilename)
    profile_conf_file = join(DEFAULT_PROFILE_DIR,profilename+".json")
    profile_conf = dict(profile_template)
    profile_conf['name']= profilename
    mkdirIfNotExist(profile_home)
    for d in profile_conf["home_dirs"]:
        mkdirIfNotExist(join(profile_home,d))
    saveProfile(profile_conf, profile_conf_file)


def getProfile(profilename):
    profile = loadProfile(profilename)
    if profile == None:
        profile = createProfile(profilename)

    return profile



def loadProfile(profilename):
    """
    loads profile from json file
    :param profilename: profile name:
    :return: - Profile instance
             - None in case profile not found
    :raises:
            - ValuerError: Profile name should be alphanumerical and less than 20 characters
            - IOError: Access error
    """
    if not RG_PROFILE.match(profilename):
        raise ValueError("Profile name should be alphanumerical and less than 20 characters",None)
    profile_conf_file = join(DEFAULT_PROFILE_DIR, profilename + ".json")
    profile_dir = join(DEFAULT_PROFILE_DIR,profilename)
    if isfile(profile_conf_file) and isdir(profile_dir):
        try:
            fin = open(profile_conf_file,"r")
            data = fin.read()
            conf = json.loads(data)
            fin.close()
            return conf,profile_dir
        except IOError, e:
            logger.error("Error loading profile conf file",)
            raise
            #raise ProfileException("Error loading profile conf file: " + profile_conf_file,e)
    logger.info("Profile not found; profilename=%s", profilename)
    return None

class Profile:
    """
    Profile class:
        -Attributes:
            - options: graphic, audio, randomuid, alwaysupdate, homedirs, download_dir, default_update etc...
            - profilename
            - profiledir
        -Methods:
            -init()
    """
    profilename = ""
    options = dict()
    profiledir = ""
    def __init__(self):
        pass



class ProfileException(Exception):
    """
    ProfileException class:
        :Gist: exception with message & cause
    """
    def __init__(self, message, cause):
        super(ProfileException, self).__init__(message + ', caused by ' + repr(cause))
        self.cause = cause

