from mongoengine import *
from config import DATABASE_HOST, DATABASE_LOGIN, DATABASE_NAME, DATABASE_PASSWORD, DATABASE_PORT

connect(DATABASE_NAME, host=DATABASE_HOST, port=DATABASE_PORT, username=DATABASE_LOGIN, password=DATABASE_PASSWORD)
print('Connected to {0}'.format(DATABASE_NAME))
