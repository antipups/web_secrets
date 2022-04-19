from dotenv import load_dotenv
import os


load_dotenv('./.env')

SECRET_KEY = os.environ.get('SECRET_KEY')
DB_host = os.environ.get('DB_host')
DB_database = os.environ.get('DB_database')
DB_user = os.environ.get('DB_user')
DB_password = os.environ.get('DB_password')
DB_char_set = os.environ.get('DB_char_set')
DB_port = os.environ.get('DB_port')

levels_config_to_file = ('DEBUG', 'ERROR', 'SUCCESS', 'CRITICAL')
