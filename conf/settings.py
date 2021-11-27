from pathlib import Path
from dotenv import load_dotenv
from urllib import parse
import os

load_dotenv('.env')

BASE_DIR = Path(__file__).resolve().parent.parent

LOG_DIR = BASE_DIR / 'logs'

if not LOG_DIR.exists(): LOG_DIR.os.makedirs(parents=True)

# MySQL
MYSQL_HOST = os.getenv('MYSQL_HOST')
MYSQL_PORT = os.getenv('MYSQL_PORT')
MYSQL_USER = os.getenv('MYSQL_USER')
MYSQL_PASSWORD = parse.quote_plus(str(os.getenv('MYSQL_PASSWORD')))
MYSQL_DATABASE = os.getenv('MYSQL_DATABASE')

class Config(object):

    JSON_AS_ASCII = False
    JOSN_SORT_KEYS = False
    JSONIFY_MIMETYPE = 'application/json;charset=utf-8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = os.getenv('SECRET_KEY')

class DevlopmentConfig(Config):

    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql:// \
                        {MYSQL_USER}:{MYSQL_PASSWORD}@ \
                        {MYSQL_HOST}:{MYSQL_PORT}/ \
                        {MYSQL_DATABASE}?charset=utf8mb4'

class ProductionConfig(Config):
    pass
