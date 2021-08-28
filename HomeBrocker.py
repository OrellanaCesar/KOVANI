from pyhomebroker import HomeBroker
from Excel import  Excel

class HomeBrocker(object):
    def __init__(self,broker, dni, user, password ):
        self.__user = user
        self.__dni = dni
        self.__password = password
        self.__broker = broker
        self.__excel = Excel()
        self.__options = excel.get_sheet()



    def get_user(self):
        return self.__user


    def set_user(self,user):
        self.__user = user


    def get_dni(self):
        return self.__dni


    def set_dni(self, dni):
        self.__dni = dni


    def get_password(self):
        return self.__password


    def set_password(self, password):
        self.__password = password


    def get_broker(self):
        return self.__broker


    def set_broker(self, broker):
        self.__broker = broker
