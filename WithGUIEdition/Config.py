import configparser
import os
conf = configparser.ConfigParser()
def ReadConf():
    return conf.read(os.getcwd() + "\\Offsets\\offsets.ini")