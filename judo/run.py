__author__ = 'xaled'
from profile import Profile



class Run:
    def __init__(self, profile, args):
        """

        :param profile: Profile instance
        :param args: user arg vector
        """
        self.__profile = profile
        self.__args = args


    def init(self, config=None):
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
