from flask import Flask, request, jsonify, render_template, session, redirect, url_for, session
import requests
import pandas as pd
import numpy as np
from my_model.predict import make_prediction


app = Flask(__name__, template_folder='template')
@app.route('/',  methods = ['GET','POST'])
def home():
    if request.method == 'POST':  
        # Get values through input bars
        age = request.form.get('age')
        sex = request.form.get('sex')
        bmi = request.form.get('bmi')
        smoker = request.form.get('smoker')
        region = request.form.get('region')
        children = request.form.get('children')
        # Put inputs to dataframe
        X = pd.DataFrame([[age, sex, bmi, smoker, region, children]], columns = ['age', 'sex', 'bmi', 'smoker', 'region', 'children'])
        # Get prediction
        prediction = make_prediction(input_data=X)
    else:
        prediction = ""
    #if prediction == 1:
    #    prediction = "male"
    #else:
    #    prediction = "female"
    return render_template("website.html", output=prediction)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int('5000'))