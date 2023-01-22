# reads common data from ini(config.ini) file.for every variable we have to create one method

import configparser

config = configparser.RawConfigParser() # to read data from ini file
config.read(".\\Configurations\\config.ini") #read from ini file

class ReadConfig():

    @staticmethod # we can access directly
    def getApplicationURL():
        url = config.get('common info','baseURL')
        return url

    @staticmethod
    def getUseremail():
        username=config.get('common info','username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info','password')
        return password
