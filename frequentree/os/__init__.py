__author__ = 'xaled'
from subprocess import Popen, PIPE

def executeCommand(cmd_vector, cwd=None, env=None, shell=False):
    """

    :param cmd_vector: command vector, example: ['ls', '-alh']
    :param cwd: working dir, example:  '/home/user1'
    :param env: envorionnemnt dict
    :param shell: use shell or not
    :return: return code of execution
    """
    #TODO: logging
    proc = Popen(cmd_vector,cwd=cwd, env=env,shell=shell)
    proc.wait()
    return proc.returncode

