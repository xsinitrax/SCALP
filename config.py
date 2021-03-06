#app version
VERSION = 1

HOST = "127.0.0.1"
PORT = "4000"
# debug
DEBUG = True

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'bmp'])

# CREATE DB FROM DUMP FILE
CREATE_DB = True
DUMP_FILE_PATH = "db"

# Define the application directory
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Define the database - we are working with
DATABASE_CONFIG = {
    'host': '127.0.0.1',
    'dbname': 'bbd',
    'user': 'bbd',
    'password': '1q2w3e4r',
    'port': 5432
}

# multi thread rendering, cuz we can
THREADS_PER_PAGE = 2

# cross site protection on
CSRF_ENABLED = True
# secret is not so secret but its just a random project xD
CSRF_SESSION_KEY = "secret"

# data path
DATA_PATH = "/src/app/static/ISIC/"

# ML vars
PREDICTOR = {
    'img_mean': [27.99144619, 19.51839209, 16.42992409],
    'img_std': [64.7680645, 47.09696396, 41.13751611],
    'img_target_size': (96, 128),
    'model_path': os.path.join(BASE_DIR,'CNN/models/CNN_binary_v1.h5')
}

IMPORT = "dump" #json does import json / dump does dump db