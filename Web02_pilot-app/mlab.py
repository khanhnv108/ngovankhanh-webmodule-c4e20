import mongoengine

# mongodb://admin:Khanh123@ds125872.mlab.com:25872/muadongkhonglanh-c4e20

host = "ds125872.mlab.com"
port = 25872
db_name = "muadongkhonglanh-c4e20"
user_name = "admin"
password = "Khanh123"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)
