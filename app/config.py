import os

SECRET_KEY = 'alura'
MYSQL_HOST = os.environ.get('MYSQL_HOST')
MYSQL_USER = os.environ.get('MYSQL_USER')
MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD')
MYSQL_DB = os.environ.get('MYSQL_DB')
MYSQL_PORT = 3306
UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'
