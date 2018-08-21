from flask import Flask, render_template, redirect
app = Flask(__name__)


@app.route('/')
def index():
    return "Ngô Văn Khánh"

@app.route('/about-me')
def about_me():
    post = {
        "title" : "Ngô Văn Khánh",
        "school" : "School: UNETI",
        "age" : "Age: 20",
        "trich_dan" : "Book: Người trộm bóng - Marc Levy",
        "fav_film" : "Film: Titanic, Mộ đom đóm"

    }
    return render_template('about_me.html',post=post)

@app.route('/school')
def school():
    return redirect("http://techkids.vn")


if __name__ == '__main__':
  app.run(debug=True)
 