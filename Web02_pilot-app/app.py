# from flask import Flask, render_template
from flask import *
import mlab
from mongoengine import *
from models.service import Service
from models.customer import Customer
from models.user import User
from models.order import Order
from datetime import datetime
from gmail import GMail, Message




app = Flask(__name__)
app.secret_key ="a super super secret key"

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
        height = form['height']
        address = form['address']
        description = form['description']
        measurements = form['measurements']

        service_update.update(
            set__name = name,
            set__yob = yob,
            set__phone = phone,
            set__height = height,
            set__address = address,
            set__description = description,
            set__measurements = measurements
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
        gender = form['gender']
        address = form['address']
        height = form['height']

        new_service = Service(
            name = name,
            yob = yob,
            phone = phone,
            gender = gender,
            address = address,
            height = height
        )

        new_service.save()

        return redirect(url_for('admin'))

        # return"St posted"


        # html set default input value
        # html radio button

@app.route('/detail/<service_id>')
def detail(service_id):
    service_detail = Service.objects.with_id(service_id)
    session["service_detail"]=str(service_detail.id)

    if "loggedin" in session:
        if session["loggedin"] == True:
            if service_detail is not None:
                return render_template("detail.html",service_detail=service_detail)
            else:
                return "Service not found"
        else:
            return redirect(url_for("logIn"))
    else:
        return redirect(url_for("logIn"))


@app.route('/sign-in',methods=["GET","POST"])
def signIn():
    if request.method == "GET":

        return render_template('signIn.html')

    elif request.method == "POST":

        form = request.form 

        fullname = form['fullname']
        email = form['email']
        username = form['username']
        password = form['password']

        user = User(
            fullname = fullname,
            email = email,
            username = username,
            password = password

        )
        user.save()

        return redirect(url_for('index'))

@app.route('/log-in',methods=["GET","POST"])
def logIn():
    if request.method == "GET":
        return render_template('logIn.html')
    elif request.method == "POST":
        form = request.form 
        username = form['username']
        password = form['password']

        found_user =User.objects(username=username,password=password)
        if found_user:
            found_user =User.objects.get(username=username,password=password)
            session['user'] = str(found_user.id)
        
            session['loggedin'] = True
            service_id = session["service_detail"]
            return redirect(url_for("detail", service_id=service_id))
        else:
            return redirect(url_for('logIn'))


@app.route('/log-out')
def logOut():
    session['loggedin'] = False
    return redirect(url_for('index'))

@app.route('/order')
def order():
    if "loggedin" in session:
        if session['loggedin'] == True:
            service = session['service_detail']
            user = session['user']

            order = Order(
                user = user,
                service = service,
                time = datetime.now(),
                is_accepted = False
            )
 
            order.save()

            session['loggedin'] = False
            return "Đã gửi yêu cầu dịch vụ!"
        else:
            return redirect(url_for('logIn'))
    else:
        return redirect(url_for('logIn'))


@app.route('/order-page')
def orderPage():
    all_order = Order.objects()

    return render_template('orderpage.html', all_order=all_order)

@app.route('/accepted/<order_id>')
def accepted(order_id):
    order = Order.objects.with_id(order_id)
    order.update(set__is_accepted = True)

    email_user = order.user.email


    gmail = GMail('ngovankhanh108@gmail.com','Khanhart108')

    html_to_send =""" Yêu cầu của bạn đã được xử lý,
    chúng tôi sẽ liên hệ với bạn trong thời gian sớm nhất.
    Cảm ơn bạn đã sử dụng dịch vụ của ‘Mùa Đông Không Lạnh"""

    # msg = Message('Test Message',to=email_user,html=html_to_send)
    msg = Message('Test Message',to='khanhnv100898@gmail.com',html=html_to_send)

    gmail.send(msg)

    return redirect(url_for('orderPage'))




if __name__ == '__main__':
  app.run(debug=True)
 