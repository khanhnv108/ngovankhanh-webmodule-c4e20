from mongoengine import *

#Design pattern (MVC, MVP)
#Design database
class Service(Document):
    image = StringField()
    name = StringField()
    yob = IntField()
    gender = IntField()
    height = IntField()
    phone = StringField()
    address = StringField()
    status = BooleanField()
    description = StringField()
    measurements = ListField()
    
