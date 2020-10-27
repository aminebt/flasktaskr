import os 

#grab the folder where this script lives 
basedir= os.path.abspath(os.path.dirname(__file__))


DATABASE = 'flasktaskr.db'
USERNAME='admin'
PASSWORD='admin'
WTF_CSRF_ENABLED=True
SECRET_KEY=b':m\x04\xc0S\x89A(\xf3\x06\x0cK\x11\xe8\xf1x\xf8;\x85\xcd\x00uB\xfb'

#define full path to database
DATABASE_PATH=os.path.join(basedir, DATABASE)
