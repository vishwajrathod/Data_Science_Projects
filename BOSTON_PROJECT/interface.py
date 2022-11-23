from flask import Flask,jsonify,render_template,request
from boston_dataset.utils import BostonHousePrice
import config
import numpy as np

app = Flask(__name__)

@app.route('/')
def home():
    return 'Successfull'

@app.route('/price')
def price():
    user_data = request.form
    crim = eval(user_data["CRIM"])
    zn = eval(user_data["ZN"])
    indus = eval(user_data["INDUS"])   
    chas = eval(user_data["CHAS"])   
    nox = eval(user_data["NOX"])    
    rm = eval(user_data["RM"])
    age = eval(user_data["AGE"])
    dis = eval(user_data["DIS"])
    rad = eval(user_data["RAD"])
    tax = eval(user_data["TAX"])
    ptratio = eval(user_data["PTRATIO"])
    b = eval(user_data["B"])
    lstat = eval(user_data["LSTAT"])

    price_obj = BostonHousePrice(crim,zn,indus,chas,nox,rm,age,dis,rad,tax,ptratio,b,lstat)
    value = price_obj.get_prediction()
    return jsonify({'Result':f"Predicted Price is : {value}"})

if __name__ == "__main__":
    app.run(port=config.PORT_NUMBER)