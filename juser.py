#!/usr/bin/python
__author__ = 'xaled'

import os
import json
import re
import random
import sys


JU_DIR = os.path.join(os.getenv("HOME"),".judo")
JU_PROFILES_DIR = os.path.join(JU_DIR, "profiles")
JU_USERLOCKS_DIR = os.path.join(JU_DIR, "userlocks")
JU_TMP_DIR = "/tmp/judo_temphomes" #os.path.join(JU_DIR, "temphomes")
JU_DOWNLOAD_DIR = os.path.join(JU_DIR, "downloads")
DEFAULT_COMMAND = "firefox"
DEFAULT_PROFILE = "default"
DEFAULT_PROFILE_CONF = {"randomuid":True, "graphic":True, "audio":True, "home_dirs":["Downloads"], "default_update":[], "download_dir":"Downloads", "alwaysupdate":False}
UID_BASE = 8801
RG_PROFILE = re.compile('^[a-z][a-z0-9_]{2,20}$',re.IGNORECASE|re.DOTALL)
RANDOM_STRING_CHARS = "abcdefghijklmnopqrstuvwxyz"
RANDOM_STRING_LEN = 4
RANDOM_STRING_PREFIX = 'ju_'
SCRIPT_DIR = "/usr/bin" #os.path.dirname(os.path.realpath(__file__))
SCRIPT_INITWP = os.path.join(SCRIPT_DIR,'juser_initwp.sh')
SCRIPT_REMOVEWP = os.path.join(SCRIPT_DIR,'juser_removewp.sh')
XAUTHFILE = os.getenv("XAUTHORITY")



def generateRandomDirName(profilename, uid, pid):
    return RANDOM_STRING_PREFIX+ ''.join(random.choice(RANDOM_STRING_CHARS) for i in range(RANDOM_STRING_LEN))+"%s.%d.%d"%(profilename,uid,pid)


def getProfiles(): #TODO:
    pass

def getProfile(profilename):
    if not RG_PROFILE.match(profilename):
        print "Profile name should be alphanumerical and less than 20 characters"
        return None
    profile_conf_file = os.path.join(JU_PROFILES_DIR, profilename + ".json")
    profile_dir = os.path.join(JU_PROFILES_DIR,profilename)
    if os.path.isfile(profile_conf_file) and os.path.isdir(profile_dir):
        try:
            fin = open(profile_conf_file,"r")
            data = fin.read()
            #print "data: ", data
            conf = json.loads(data)
            fin.close()
            return conf,profile_dir
        except :
            print "Error loading profile conf file: " , profile_conf_file
            #return None
    return None


def mkdirIfNotExist(dir):
    if  not os.path.isdir(dir):
        os.mkdir(dir)


def initJU():
    mkdirIfNotExist(JU_DIR)
    mkdirIfNotExist(JU_PROFILES_DIR)
    mkdirIfNotExist(JU_USERLOCKS_DIR)
    mkdirIfNotExist(JU_TMP_DIR)
    os.system("chmod 1777 '%s'"%(JU_TMP_DIR))
    mkdirIfNotExist(JU_DOWNLOAD_DIR)

    #if getProfile(DEFAULT_PROFILE) == None:
    #    createProfile(DEFAULT_PROFILE)

def cleanJU(): #TODO
    pass

def saveProfile(profile_conf, profile_conf_file):
    fou = open(profile_conf_file,"w")
    fou.write(json.dumps(profile_conf,indent=3))
    fou.close()


def createProfile(profilename):
    profile_home = os.path.join(JU_PROFILES_DIR, profilename)
    profile_conf_file = os.path.join(JU_PROFILES_DIR,profilename+".json")
    profile_conf = dict(DEFAULT_PROFILE_CONF)
    profile_conf['name']= profilename
    mkdirIfNotExist(profile_home)
    for d in profile_conf["home_dirs"]:
        mkdirIfNotExist(os.path.join(profile_home,d))
    saveProfile(profile_conf, profile_conf_file)


def editProfileConf(profilename):
    if getProfile(profilename) != None:
        os.system("editor '%s'"(os.path.join(JU_PROFILES_DIR,profilename+".json")))




def cloneProfile(oldProfile, newProfile): #TODO:
    pass

def isValidUID(uid):
    uidlockfile = os.path.join(JU_USERLOCKS_DIR,str(uid) + ".lock")
    if os.path.exists(uidlockfile):
        return False #TODO: verify pid
    else:
        return True

def saveUIDlock(uid):
    uidlockfile = os.path.join(JU_USERLOCKS_DIR,str(uid) + ".lock")
    fou =  open(uidlockfile,"w")
    pid = os.getpid()
    fou.write(str(pid))
    fou.close()

def removeUIDlock(uid):
    uidlockfile = os.path.join(JU_USERLOCKS_DIR,str(uid) + ".lock")
    os.unlink(uidlockfile)

def generateRandomUID():
    uid = random.randint(0,100) + UID_BASE
    while( not isValidUID(uid)):
        uid = random.randint(0,100) + UID_BASE

    return uid

def getSudoRight(uid):
    os.system("gksudo -u ju%s id"%(uid))


def initWorkPath(uid,profiledir,homedir):
    #giving temp permission to copy dir
    os.system("/bin/chmod go+rx '%s'"%(profiledir))

    #make and copy dir

    runCommand(uid,homedir,SCRIPT_INITWP + " " + homedir + " " + profiledir)

    #removing permissions on profiledir
    os.system("/bin/chmod go-rwx '%s'"%(profiledir))
    #return homedir

def removeWorkpath(uid,workpath):
    runCommand(uid,workpath,SCRIPT_REMOVEWP + " " + workpath)

def initpermissions(uid, profileconf):  #TODO
    groups = "judo"
    if profileconf['graphic']== True:
        os.system("/usr/bin/xhost '+si:localuser:#%d'"%(uid))
        groups += ",judog"
    if profileconf['audio']==True:
        groups += ",audio"
    os.system("sudo /usr/bin/ju_usermod %s %s"%(uid,groups))


def removePermissions(uid, profileconf): #TODO
    if profileconf['graphic']== True:
        os.system("/usr/bin/xhost '-si:localuser:#%d'"%(uid))

def runCommand(uid,workpath,cmd,cd=False):
    current_pwd = os.curdir
    bash_c = '"export HOME=\'%s\'; %s; "'%(workpath,cmd)
    #command = "/usr/bin/sudo -u '#%s' -g 'audio' bash -c %s;"%(uid,bash_c)
    command = "/usr/bin/sudo -u ju%s bash -c %s;"%(uid,bash_c)
    if cd: command = "cd '%s' ;"%(workpath) + command + " cd '%s';"%(current_pwd)
    print "sudo command: ", command
    os.system(command)
"""
def runCommand(uid,workpath,cmd,cd=False):
    command = "/usr/bin/sudo -u ju%s %s;"%(uid,cmd)
    print "sudo command: ", command
    os.system(command)"""

def syncDir(source, destination):
    rsync_cmd = "/usr/bin/rsync -r '%s/' '%s'"%(source,destination)
    print rsync_cmd
    os.system(rsync_cmd)

def syncFile(source, destination):
    rsync_cmd = "/usr/bin/rsync '%s' '%s'"%(source,destination)
    print rsync_cmd
    os.system(rsync_cmd)

def createUser(uid,workpath):
    os.system("sudo /usr/bin/ju_useradd %s '%s'"%(uid,workpath))

def removeUser(uid):
    os.system("sudo /usr/bin/ju_userdel %s"%(uid))

def killallprocess(uid,workpath):
    runCommand(uid,workpath,"pkill -9 -u ju%s"%(uid))

def getWorkDir(profilename,uid):
    randomdirname = generateRandomDirName(profilename,uid,os.getpid())
    homedir = os.path.join(JU_TMP_DIR,randomdirname)
    print "temp homedir: ", homedir
    return homedir

def juserMain(cmd=DEFAULT_COMMAND, profilename=DEFAULT_PROFILE, update=False):
    if getProfile(profilename) == None:
        createProfile(profilename)

    profileconf,profiledir = getProfile(profilename)
    uid = generateRandomUID()
    saveUIDlock(uid)
    #getSudoRight(uid)
    workpath = getWorkDir(profilename,uid)
    createUser(uid,workpath)

    initWorkPath(uid,profiledir,workpath) # sudo
    print "workpath: ", workpath

    initpermissions(uid, profileconf)

    runCommand(uid,workpath,cmd,cd=False) #sudo, graphic

    #chmod workpath before rsyncing
    runCommand(uid,workpath,"find '%s' -type d -exec chmod go+rx {} \\;"%(workpath),cd=False)
    runCommand(uid,workpath,"find '%s' -type f -exec chmod go+r {} \\;"%(workpath),cd=False)
    syncDir(os.path.join(workpath,profileconf['download_dir']),JU_DOWNLOAD_DIR)
    if update or profileconf['alwaysupdate']:
        syncDir(workpath,profiledir)
    else:
        for ud in profileconf['default_update']:
            abs_path1 = os.path.join(workpath,ud)
            abs_path2 = os.path.join(profiledir,ud)
            if os.path.isdir(abs_path1):
                syncDir(abs_path1,abs_path2)
            elif os.path.isfile(abs_path1):
                syncFile(abs_path1,abs_path2)
    removePermissions(uid, profileconf)
    removeWorkpath(uid,workpath) # sudo
    #killallprocess(uid,workpath) #sudo
    removeUser(uid)
    removeUIDlock(uid)

def quote_argument(argument):
    return '"%s"' % (
        argument
        .replace('\\', '\\\\')
        .replace('"', '\\"')
        .replace('$', '\\$')
        .replace('`', '\\`')
    )


if __name__ == "__main__":
    #runCommand(8801,"/home/walop","env")
    #"""

    initJU()
    if len(sys.argv) <3 or (sys.argv[1]=='-u' and len(sys.argv)< 4):
        print "usage: judo  [-u] profile command"
        #juserMain()
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
            juserMain(cmd=cmd,profilename=profile,update=update)

    #"""
