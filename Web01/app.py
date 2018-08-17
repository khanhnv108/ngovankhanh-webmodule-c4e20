# fapp + tab 

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    posts =[
        {
            'title': "Thơ con cóc",
            'content':"Hôm nay trăng lên cao quá",
            'author':"K",
            'author_sex':0
        },
        {
            'title': "Thơ lập trình",
            'content':"Thầy bảo em viết bài Thơ",
            'author':"DHT",
            'author_sex':1
        }
    ]
    return render_template('index.html',posts=posts)

@app.route('/hello')
def say_hello():
    return "Hello from the other side"

@app.route('/say-hi/<name>/<age>')
def say_hi(name,age):
    return "Hi {}, you 're {} years old ".format(name,age)

@app.route('/sum/<int:a>/<int:b>')
def sum_ab(a , b):
    return str(a + b)

if __name__ == '__main__':
  app.run(debug=True)
 