from mongoengine import *
import mongoengine

# mongodb://admin:admin@ds021182.mlab.com:21182/c4e

host = "ds021182.mlab.com"
port = 21182
db_name = "c4e"
user_name = "admin"
password = "admin"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

connect()

class River(Document):
    name = StringField()
    continent = StringField()
    length = IntField()


# all_river = River.objects(continent__contains='Africa')

# for river in all_river:
#     print("{} -{} - {}".format(river.name,river.continent,river.length))


all_river = River.objects(continent__contains='S.America', length__lt=1000)
for river in all_river:
    print("{} -{} - {}".format(river.name,river.continent,river.length))
