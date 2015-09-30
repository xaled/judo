__author__ = 'xaled'

from os.path import isdir
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
    if ret != 0: raise SomeEror("command failed with return code:%d"%(ret))
    if chmod != None:
        executeCommand(['chmod','-R',dir,chmod])

def createLink(src,dst,chmod=None, chown=None):
    ret = executeCommand(['ln','-s',src,dst])
    if chmod != None:
        executeCommand(['chmod',dst,chmod])
    if chown != None:
        executeCommand(['chown',dst,chown])
