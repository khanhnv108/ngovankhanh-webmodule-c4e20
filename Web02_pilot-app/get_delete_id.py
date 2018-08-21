import mlab
from mongoengine import *
from models.service import Service



mlab.connect()

# service = Service.objects(id = "5b781d5c5b2e871e5497a993")
# service = Service.objects.get(id = "5b781d5c5b2e871e5497a993")
service = Service.objects(pk = "5b781d5c5b2e871e5497a993")
print(service)


# service = Service.objects.get( id ="5b781f215b2e8709d8fc502d" )
# service.delete()

