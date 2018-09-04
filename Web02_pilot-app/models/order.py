from mongoengine import *


class Order(Document):
    service = ReferenceField("Service")
    user = ReferenceField("User")
    time = DateTimeField()
    is_accepted = BooleanField()