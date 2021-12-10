import os

from dotenv import load_dotenv


load_dotenv()

POSTGRES_URL = os.environ.get('POSTGRES_URL')
POSTGRES_NAME = os.environ.get('POSTGRES_NAME')
POSTGRES_USER = os.environ.get('POSTGRES_USER')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
POSTGRES_HOST = os.environ.get('POSTGRES_HOST')
POSTGRES_PORT = os.environ.get('POSTGRES_PORT')

DEBUG = os.environ.get('DEBUG', '') != 'False'
