__author__ = 'xaled'
from profile import Profile



class Run:
    def __init__(self, profile,cmd, args):
        """

        :param profile: Profile instance
        :param cmd: command string list
        :param args: user arg vector
        """
        self.__profile = profile
        self.__args = args
        self.__cmd = cmd


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
        self.__create_profile_lock()
        self.__create_user()
        self.__set_permissions()
        self.__prepare_homedir()



    def execute(self):
        """
        execute command in under jailed user, using sudo
        script:
        cd $workpath; # if necessary
        export HOME=$home
        sudo -u ju$uid $cmd
        cd $original # if necessary
        """
        pass

    def clean(self):
        pass


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
        pass

    def __create_profile_lock(self):
        """

        :return:
        """
        pass

    def __getuid(self):
        """

        :return:
        """
        pass

    def  __create_user(self):
        """

        :return:
        """
        pass

    def __set_permissions(self):
        """

        :return:
        """
        pass

    def __prepare_homedir(self):
        """

        :return:
        """
        pass
