from pathlib import Path
import configparser

config_ini = configparser.ConfigParser()
config_ini.read('config.ini', encoding='utf-8')

DIRECTORY = Path(config_ini['data']['directory']).expanduser()
