from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return "Hello"

@app.route('/user/<username>')
def name(username):
    users ={
        "quan": {
            "name":"Nguyen Anh Quan",
            "age":16,
            "gender":"Male"
        },
        "tuananh": {
            "name":"Huynh Tuan Anh",
            "age":23,
            "gender":"Male"
        },
        "bich": {
            "name":"Nguyen Bich",
            "age":20,
            "gender":"Female"
        },
        "khanh": {
            "name":"Ngo Van Khanh",
            "age":15,
            "gender":"Male"
        }
    }

    if username in users:
        return render_template('name.html',username = users[username])
    else:
        return "User not found"

if __name__ == '__main__':
  app.run(debug=True)
 