import mlab
from models.service import Service

mlab.connect()

# all_service = Service.objects()

# first_service = all_service[0]

# print(first_service['name'])


id_to_find ="5b7ed0bc5b2e870660889f1b"

# hera = Service.objects(id = id_to_find) ## => [Service obj]
# hera = Service.objects.get(id = id_to_find) ## => Service obj
service = Service.objects.with_id(id_to_find)  ## => Service obj



# if service is not None:
#     service.delete()
#     print("Deleted")
#     print("Before")
#     print(service.to_mongo())
#     service.update(set__yob=2001, set__name="Linh")
#     service.reload()
#     print("After")
#     print(service.to_mongo())
# else:
#     print("Not found")
