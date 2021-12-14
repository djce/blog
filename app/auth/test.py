from pathlib import Path

import configparser


BASE_DIR = Path(__file__).resolve().parent.parent

config = configparser.ConfigParser()

# [section]
# option = value

config.read(BASE_DIR / 'conf/my.ini',encoding='utf-8')

# config.read_file()

# 解析字典
# config.dict({'section': {'option': 'value'}})


# 获取全部sctions
config.sections()

# section是否存在
config.has_section(section='base')

# 获取指定section的options的keys
keys = config.options(section='base')


# 获取属性
scheduler = config.get('base', 'scheduler')





