import os
from app import create_app


app = create_app(os.getenv('AGRIB_CONFIG') or 'default')

