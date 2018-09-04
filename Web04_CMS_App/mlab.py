import mongoengine

# mongodb://admin:Khanh123@ds115219.mlab.com:15219/cms-app-c4e20

host = "ds115219.mlab.com"
port = 15219
db_name = "cms-app-c4e20"
user_name = "admin"
password = "Khanh123"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)
