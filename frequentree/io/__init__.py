__author__ = 'xaled'

from os.path import isdir
from os import mkdir


def mkdirIfNotExist(dir):
    if  not isdir(dir):
        mkdir(dir)