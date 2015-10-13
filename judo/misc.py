__author__ = 'xaled'


from frequentree.os import executeCommand

def usermod(uid, append_groups):
    executeCommand(['usermod', '-aG',append_groups])


def addXhostPermission(uid):
    #os.system("/usr/bin/xhost '+si:localuser:#%d'"%(uid))
    executeCommand(['/usr/bin/xhost','+si:localuser:#%d'%(uid)])