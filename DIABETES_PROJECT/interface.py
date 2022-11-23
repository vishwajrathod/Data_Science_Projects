from flask import Flask,render_template,jsonify,request
from Diabetes_data.utils import Diabetes
import config

app = Flask(__name__)

@app.route('/')
def home():
    return "Success"

@app.route('/predicted_diabetes')
def get_predicted_diabetes():
    data = request.form
    age = eval(data['age'])
    sex = eval(data['sex'])
    bmi = eval(data['bmi'])
    bp = eval(data['bp'])
    s1 = eval(data['s1'])
    s2 = eval(data['s2'])
    s3 = eval(data['s3'])
    s4 = eval(data['s4'])
    s5 = eval(data['s5'])
    s6 = eval(data['s6'])
    diab_obj = Diabetes(age, sex, bmi, bp, s1, s2, s3, s4, s5, s6)
    predicted_diabetes = diab_obj.get_predicted_diabetes()
    return jsonify({"Result":f"Predicted diabetes is : {predicted_diabetes}"})

if __name__ == "__main__":
    app.run(port=config.PORT_NUMBER)