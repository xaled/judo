__author__ = 'xaled'

from os.path import isdir
from os import mkdir
from shutil import rmtree, copytree


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