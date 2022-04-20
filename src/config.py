from pathlib import Path
import configparser

config_ini = configparser.ConfigParser()
config_ini.read('config.ini', encoding='utf-8')

def str2bool(s):
    return s.lower() in "true yes t 1".split()
        
DIRECTORY = Path(config_ini['data']['directory']).expanduser()
FILENAME = Path(config_ini['data']['filename'])
ROTATE = int(config_ini['data']['rotate'])
