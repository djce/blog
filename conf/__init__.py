from .settings import DevlopmentConfig, ProductionConfig
import os

def load_config(mode=os.getenv('FLASK_CONF')):

    if mode == 'dev':
        return DevlopmentConfig
    elif mode == 'prod':
        return ProductionConfig
    else:
        return DevlopmentConfig
