import os

JSON_MIME_TYPE = 'application/json'

DB_CONF = {
    'user': 'root',
    'password': '123',
    'host': os.environ.get('IP', '0.0.0.0'),
    'database': 'recipes-project'
}

class DevelopmentConfig:

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8'.format(
      **{
        'user': os.getenv('DB_USER', DB_CONF['user']),
        'password': os.getenv('DB_PASSWORD', DB_CONF['password']),
        'host': os.getenv('DB_HOST', DB_CONF['host']),
        'database': os.getenv('DB_DATABASE', DB_CONF['database'])
    })
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False

Config = DevelopmentConfig

