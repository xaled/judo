__author__ = 'xaled'

from os.path import isdir, exists
from os import mkdir
from shutil import rmtree, copytree
from ..os import executeCommand


def mkdirIfNotExist(dir):
    if  not isdir(dir):
        mkdir(dir)


def appendToTextFile(txt,file):
    with open(file,"a") as fou:
        fou.write(txt)
        fou.close()


def writeToTextFile(txt,file):
    with open(file,"w") as fou:
        fou.write(txt)
        fou.close()


def removeDir(dir):
    rmtree(dir, ignore_errors=True)

def copyDir(src,dst):
    copytree(src,dst,symlinks=True)

def chownDir(dir, usr, grp, chmod=None):
    ret = executeCommand(['chown','%s:%s'%(usr,grp),'-R',dir]) #TODO: usr,grp validate
    if ret != 0: raise RuntimeError("chown command failed with return code:%d"%(ret))
    if chmod != None:
        ret2 = executeCommand(['chmod','-R',dir,chmod])
        if ret2 != 0: raise RuntimeError("chmod command failed with return code:%d"%(ret2))

def setfacl(path, user=None, group=None, default=False, perms="---"):
    #TODO validate perms, user & group
    if not exists(path):
        return #Log error!
    if user==None and group==None:
        return
    elif user!=None:
        perms_string = "u:%s:%s"%(user,perms)
    else:
        perms_string = "g:%s:%s"%(group,perms)
    executeCommand(['setfacl',"-m",perms_string, path])
    if isdir(path) and default==True:
        executeCommand(['setfacl',"-m","d:"+perms_string, path])


def createLink(src,dst,chmod=None, chown=None):
    ret = executeCommand(['ln','-s',src,dst])
    if chmod != None:
        executeCommand(['chmod',dst,chmod])
    if chown != None:
        executeCommand(['chown',dst,chown])
