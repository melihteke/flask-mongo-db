import os
import sys
import pathlib
from dotenv import load_dotenv


dotenv_current_path = os.path.join(pathlib.Path().resolve(), '.env')
load_dotenv(dotenv_current_path)

DB_URI = os.environ.get("DB_URI")
DB_NAME = os.environ.get("DB_NAME")
DB_COLLECTION_NAME = os.environ.get("DB_COLLECTION_NAME")
