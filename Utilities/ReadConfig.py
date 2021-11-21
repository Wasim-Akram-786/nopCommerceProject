import configparser

config=configparser.RawConfigParser()
config.read('.//Configuration//config.ini')

class ReadConfig:
    @staticmethod
    def url():
        url=config.get('common info','url')
        return url
    @staticmethod
    def username():
        username=config.get('common info','username')
        return username
    @staticmethod
    def password():
        password=config.get('common info','password')
        return password
