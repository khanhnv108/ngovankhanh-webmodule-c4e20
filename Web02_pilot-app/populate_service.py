from models.service import Service
import mlab
from faker import Faker
from random import randint,choice



mlab.connect()

fake = Faker()

# for i in range(10):
#     print("Saving service", i +1, ".........")
#     new_service = Service(
#         image = 
#         name = fake.name(),
#         yob = randint(1991,1999),
#         gender = randint(0,1),
#         height = randint(150,190),
#         phone = fake.phone_number(),
#         address = fake.address(),
#         status = choice([True,False])
#         description = "Ngoan, hiền, dễ thương"
#         measurements = [randint(75,90),randint(55-70),randint(75-90)]
#     )



# new_service = Service(
#     image = '../static/image/female.jpg',
#     name ="Thu Nguyễn" ,
#     yob = randint(1991,1999),
#     gender = 0,
#     height = randint(150,180),
#     phone = "0979868978",
#     address ="Hà Nội" ,
#     status = choice([True,False]),
#     description = "Ngoan, hiền, dễ thương,yêu trẻ con",
#     measurements =[90,60,90]
#     )

# new_service.save()

# new_service = Service(
#     image = "../static/image/male.jpg",
#     name ="Tuấn Anh" ,
#     yob = randint(1991,1999),
#     gender = 1,
#     height = randint(165,180),
#     phone = "0979868978",
#     address ="Cầu Giấy, Hà Nội" ,
#     status = choice([True,False]),
#     description = "Yêu thẻ thao, hòa đồng, thích nuôi cún"
#     )

# new_service.save()
