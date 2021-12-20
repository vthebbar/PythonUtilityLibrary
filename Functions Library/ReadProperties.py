# To read properties from config.ini file

import configparser

config = configparser.RawConfigParser()
config.read("..\\Configuration\\Config.ini")

class Configurations:

    @staticmethod
    def get_url():
        url = config.get('common info','url')
        return url

    @staticmethod
    def get_emailid():
        email_id = config.get('common info', 'email_id')
        return email_id

    @staticmethod
    def get_password():
        password = config.get('common info','password')
        return password


# Below section is test and verify functions are working file
url= Configurations.get_url()
email= Configurations.get_emailid()
pwd = Configurations.get_password()

print(url)
print(email)
print(pwd)