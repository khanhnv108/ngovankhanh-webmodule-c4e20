from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return "Khánh"

@app.route('/bmi/<float:weight>/<float:height>')
def bmi(weight, height):
    height = height / 100
    bmi = weight /(height * height)
    if bmi < 16 :
        return 'BMI ='+ str(bmi) + ' : Severely underweight'
    elif bmi < 18.5 :
        return 'BMI ='+ str(bmi) + ' : Underweight'
    elif bmi < 25 :
        return 'BMI ='+ str(bmi) + ' : Normal'
    elif bmi < 30 :
        return 'BMI ='+ str(bmi) + ' : Overweight'
    else:
        return 'BMI ='+ str(bmi) + ' : Obese'

@app.route('/bmi_render/<float:weight>/<float:height>')
def bmi_render(weight, height):
    height = height / 100
    bmi = weight /(height * height)

    BMI = {
        "bmi" : bmi,
        "tinh_trang":""
    }

    return render_template('bmi.html',BMI=BMI)


if __name__ == '__main__':
  app.run(debug=True)
 