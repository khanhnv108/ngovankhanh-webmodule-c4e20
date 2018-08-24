# from flask import Flask, render_template
from flask import *
import mlab
from mongoengine import *
from models.service import Service
from models.customer import Customer


app = Flask(__name__)
mlab.connect()

#parameter('/asd/<asf>') request + para
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/<g>')
def search(g):
    all_service = Service.objects(gender=g)
    # all_service = Service.objects(gender=g, yob__lte=1998, height__gte=165, address__contains="Hà Nội")
    return render_template('search.html',all_service=all_service)

@app.route('/customer_full')
def customer_full():
    all_customer = Customer.objects()
    
    return render_template('customer.html',all_customer=all_customer)


@app.route('/customer/<g>')
def customer(g):
    all_customer = Customer.objects(gender=g )
    
    return render_template('customer.html',all_customer=all_customer)

@app.route('/customer_contacted/<g>')
def customer_contacted(g):
    
    all_customer = Customer.objects[0:10](gender=g, contacted = False)

    return render_template('customer_contacted.html',all_customer=all_customer)


@app.route('/admin')
def admin():
    all_service = Service.objects()
    return render_template('admin.html', all_service = all_service)

@app.route('/delete/<service_id>')
def delete(service_id):
    service_to_delete = Service.objects.with_id(service_id)

    if service_to_delete is not None:
        service_to_delete.delete()
        # return "Deleted " + service_id
        return redirect(url_for('admin'))
    else:
        return " Service not found"

@app.route('/update/<service_id>', methods=["GET","POST"])
def update(service_id):
    service_update = Service.objects.with_id(service_id)

    if request.method == "GET":
        return render_template('update.html',service_update=service_update)
    elif request.method == "POST":
        form = request.form
        name = form['name']
        yob = form['yob']
        phone = form ['phone']

        service_update.update(
            set__name = name,
            set__yob = yob,
            set__phone = phone
        )

        return redirect(url_for('admin'))



@app.route('/new-service', methods= ["GET","POST"])
def creat():
    if request.method =="GET":
        return render_template('new-service.html')
    elif request.method =="POST":
        form = request.form 
        name = form['name']
        yob = form['yob']
        phone = form['phone']
        # gender = form['gender']
        
        new_service = Service(
            name = name,
            yob = yob,
            phone = phone
            # gender = gender
        )

        new_service.save()

        return redirect(url_for('admin'))

        # return"St posted"


        # html set default input value
        # html radio button

@app.route('/detail/<service_id>')
def detail(service_id):
    all_service = Service.objects()
    service_detail = Service.objects.with_id(service_id)

    if service_detail is not None:
        # return service_id
        return render_template('detail.html',service_detail=service_detail)
    else:
        return " Not found"







if __name__ == '__main__':
  app.run(debug=True)
 