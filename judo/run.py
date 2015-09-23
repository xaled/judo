__author__ = 'xaled'
from profile import Profile
from frequentree.os import executeCommand
from frequentree.io import appendToTextFile, writeToTextFile, removeDir, copyDir
#import os
import logging, random, os
from os.path import join, exists


logger = logging.getLogger(__name__)


class Run:
    def __init__(self, profile,cmd, args):
        """

        :param profile: Profile instance
        :param cmd: command string list
        :param args: user arg vector
        """
        self.profile = profile
        self.args = args
        self.cmd = cmd
        self.pid = os.getpid()


    def init(self):
        """
        init the temp work environement:
            1- check if the same profile is running, act according to profile/user/default option
            2- create profile lock
            3- create user
            4- set permissions & jail environnement
            5- prepare temp homedir: copy profile files, create some links, etc...

        """
        if self.__is_profile_running():
            """
            #TODO
            if run & sameuid:
                  delegate()
                  return
            elif !run:
                return # exit

            """
            pass
        self.__getuid()
        self.__create_profile_lock()
        self.__create_user()
        self.__prepare_homedir()
        self.__set_permissions()




    def execute(self):
        """
        execute command in under jailed user, using sudo
        script:
            1- set working dir if necessary
            2- sudo option
            3- execute
        """
        #env = os.environ.copy()
        logger.info("running command cmd=", self.__cmd)
        sudo_cmd=list(['sudo', '--set-home'],self.__cmd)
        executeCommand(sudo_cmd, cwd=self.__workdir)


    def clean(self):
        """

        :return:
        """
        #TODO:
        """
        while(still uid process)
            if kill: killall()
            else: wait()
        """
        self.__kill_all_processes()
        self.__sync_dirs()
        self.__remove_workdir()
        self.__remove_permissions()
        self.__remove_user()


    ## init private methods:
    def __check_profile_lock(self):
        """
        :return: True if profile_lock is valid, False otherwise
        :raises: IOError
        """
        pass
    def __is_profile_running(self):
        """

        :return:
        """
        return False

    def __create_profile_lock(self):
        """

        :return:
        """
        profilelock= join(DEFAULT_LOCK_DIR, self.__profile.profilename+".lock")
        appendToTextFile(profilelock,os.getpid()+"\n")


    def __getuid(self):
        """
        generate random uid

        """
        uid = random.randint(0,1000) + DEFAULT_UID_BASE
        while( not self. __isValidUID(uid)):
            uid = random.randint(0,1000) + DEFAULT_UID_BASE

        #save uid lock
        uidlockfile = join(DEFAULT_LOCK_DIR,str(uid) + ".lock")
        writeToTextFile(str(os.getpid()),uidlockfile)
        self.uid = uid
        randomdirname = "%s.%d.%d"%(profilename,uid,self.pid) + generateRandom() #  RANDOM_STRING_PREFIX+ ''.join(random.choice(RANDOM_STRING_CHARS) for i in range(RANDOM_STRING_LEN))
        workdir = os.path.join(JUSER_ROOTDIR,randomdirname)
        logger.info("generated random uid & workdir, uid={uid} workdir={workdir}",uid=uid, workdir=workdir)
        self.workdir = workdir


    def __is_valid_uid(self,uid):
        uidlockfile = join(DEFAULT_LOCK_DIR,str(uid) + ".lock")
        if exists(uidlockfile):
            return False #TODO: verify pid
        else:
            return True

    def  __create_user(self):
        """

        :return:
        """
        cmd_vector = ["/usr/bin/useradd", "-u", str(self.uid), "-d", self.workdir, "-M", "ju%d"%(self.uid)]
        executeCommand(cmd_vector)

    def __set_permissions(self):
        """
        0- user permission over ju dirs + shares
        1- graphic permissions
        2- audio permissin
        3- netpermission
        :return:
        """


    def __prepare_homedir(self):
        """

        :return:
        """
        #TODO
        removeDir(self.workdir)
        copyDir(self.__pr)
        """
        rm workdir
        cp profiledir to workdir
        chown workdir
        make links (updatables dirs + share dirs)
        make user links
        """

    ## clean private methods:

    def __is_stillrunning_processes(self):
        """

        :return:
        """
        pass


    def __kill_all_processes(self):
        pass

    def __sync_dirs(self):
        pass

    def __remove_workdir(self):
        pass

    def __remove_permissions(self):
        pass

    def __remove_user(self):
        pass

