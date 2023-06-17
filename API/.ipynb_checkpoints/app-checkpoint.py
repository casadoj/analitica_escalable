from flask import Flask, request, jsonify, render_template, session, redirect, url_for, session
import requests
import pandas as pd
import numpy as np
from my_model.predict import make_prediction


app = Flask(__name__, template_folder='template')
@app.route('/',  methods = ['GET', 'POST'])
def home():
    if request.method == 'POST':  
        # get values through input bars
        age = request.form.get('age')
        sex = request.form.get('sex')
        bmi = request.form.get('bmi')
        children = request.form.get('children')
        smoker = request.form.get('smoker')
        region = request.form.get('region')
        # convert in puts to a DataFrame
        X = pd.DataFrame([[age, sex, bmi, children, smoker, region]], columns = ['age', 'sex', 'bmi', 'children', 'smoker', 'region'])
        # predict
        charges = make_prediction(input_data=X)['predictions'][0]
        prediction = f'The estimated cost of your insurance is {charges:.2f} €'
    else:
        prediction = ""

    return render_template("website.html", output=prediction)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int('5000'))