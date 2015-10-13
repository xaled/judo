__author__ = 'xaled'
import re, os

JU_DIR = os.path.join(os.getenv("HOME"),".judo")


# PROFILE
DEFAULT_PROFILE_CONF = {"randomuid":True, "graphic":True, "audio":True, "home_dirs":["Downloads"], "default_update":[], "download_dir":"Downloads", "alwaysupdate":False}
RG_PROFILE = re.compile('^[a-z][a-z0-9_]{2,20}$',re.IGNORECASE|re.DOTALL)
DEFAULT_PROFILE_DIR = os.path.join(JU_DIR, "profiles")
DEFAULT_LOCK_DIR = os.path.join(JU_DIR, "locks")
DEFAULT_UID_BASE = 8801
JUSER_ROOT_DIR = "/var/judo"
DEFAULT_JUSER_TEMPDIR_ROOT = os.path.join(JUSER_ROOT_DIR,"temphomes")
DEFAULT_JUDO_SHARE = os.path.join(JUSER_ROOT_DIR,"pub")
DEFAULT_JUDO_DRIVES = os.path.join(JUSER_ROOT_DIR,"drives")




# a voir

JU_DIR = os.path.join(os.getenv("HOME"),".judo")
JU_PROFILES_DIR = os.path.join(JU_DIR, "profiles")
JU_USERLOCKS_DIR = os.path.join(JU_DIR, "userlocks")
JU_TMP_DIR = "/tmp/judo_temphomes" #os.path.join(JU_DIR, "temphomes")
JU_DOWNLOAD_DIR = os.path.join(JU_DIR, "downloads")
DEFAULT_COMMAND = "firefox"
DEFAULT_PROFILE = "default"

RANDOM_STRING_CHARS = "abcdefghijklmnopqrstuvwxyz"
RANDOM_STRING_LEN = 4
RANDOM_STRING_PREFIX = 'ju_'
SCRIPT_DIR = "/usr/bin" #os.path.dirname(os.path.realpath(__file__))
SCRIPT_INITWP = os.path.join(SCRIPT_DIR,'juser_initwp.sh')
SCRIPT_REMOVEWP = os.path.join(SCRIPT_DIR,'juser_removewp.sh')
XAUTHFILE = os.getenv("XAUTHORITY")