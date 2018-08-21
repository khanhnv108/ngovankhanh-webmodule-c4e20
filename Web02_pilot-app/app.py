from flask import Flask, render_template
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
    all_service = Service.objects(gender=g,height__gte=165)
    # all_service = Service.objects(gender=g, yob__lte=1998, height__gte=165, address__icontains="Hà Nội")
    return render_template('search.html',all_service=all_service)

@app.route('/customer/<g>')
def customer(g):
    all_customer = Customer.objects(gender=g )
    
    return render_template('customer.html',all_customer=all_customer)

@app.route('/customer_contacted/<g>')
def customer_contacted(g):
    
    all_customer = Customer.objects[0:10](gender=g, contacted = False)

    return render_template('customer_contacted.html',all_customer=all_customer)




if __name__ == '__main__':
  app.run(debug=True)
 