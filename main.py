from flask import Flask, jsonify, render_template, request
from flask_cors import CORS, cross_origin
import jsonify
import pickle
import numpy
import sklearn
import requests
app = Flask(__name__)

@app.route('/', methods = ['GET'])
#@cross_origin()
def homepage():
    return render_template("index.html")

@app.route('/predict',methods=['GET','POST'])
#@cross_origin()
def index():
    if request.method == 'POST':
        try:
            age = int(request.form['age'])

            workclass = request.form['workclass']
            if workclass == 'Private':
                workclass = 3
            elif workclass == 'Self-emp-not-inc':
                workclass = 5
            elif workclass == 'Local-gov':
                workclass = 1
            elif workclass == 'State-gov':
                workclass = 6
            elif workclass == 'Self-emp-inc':
                workclass = 0
            elif workclass == 'Federal-gov':
                workclass = 4
            elif workclass == 'Without-pay':
                workclass = 7
            else:
                workclass = 2

            education = request.form['education']
            if education == 'HS-grad':
                education = 11
            elif education == 'Some-college':
                education = 15
            elif education == 'Bachelors':
                education = 9
            elif education == 'Masters':
                education = 12
            elif education == 'Assoc-voc':
                education = 8
            elif education == '11th':
                education = 1
            elif education == 'Assoc-acdm':
                education = 7
            elif education == '10th':
                education = 0
            elif education == '7th-8th':
                education = 5
            elif education == 'Prof-school':
                education = 6
            elif education == '9th':
                education = 2
            elif education == '12th':
                education = 14
            elif education == 'Doctorate':
                education = 4
            elif education == '1st-4th':
                education = 3
            else:
                education = 13

            education_num = request.form['education_num']

            marital_status = request.form['marital_status']
            if marital_status == 'Married-civ-spouse':
                marital_status = 2
            elif marital_status == 'Never-married':
                marital_status = 4
            elif marital_status == 'Divorced':
                marital_status = 0
            elif marital_status == 'Separated':
                marital_status = 5
            elif marital_status == 'Widowed':
                marital_status = 6
            elif marital_status == 'Married-spouse-absent':
                marital_status = 3
            else:
                marital_status = 1

            occupation = request.form['occupation']
            if occupation == 'Prof-specialty':
                occupation = 9
            elif occupation == 'Craft-repair':
                occupation = 2
            elif occupation == 'Exec-managerial':
                occupation = 0
            elif occupation == 'Adm-clerical':
                occupation = 3
            elif occupation == 'Sales':
                occupation = 7
            elif occupation == 'Other-service':
                occupation = 11
            elif occupation == 'Machine-op-inspct':
                occupation = 6
            elif occupation == 'Transport-moving':
                occupation = 5
            elif occupation == 'Handlers-cleaners':
                occupation = 13
            elif occupation == 'Farming-fishing':
                occupation = 12
            elif occupation == 'Tech-support':
                occupation = 4
            elif occupation == 'Protective-serv':
                occupation = 10
            elif occupation == 'Priv-house-serv':
                occupation = 8
            else:
                occupation = 1

            relationship = request.form['relationship']
            if relationship == 'Husband':
                relationship = 0
            elif relationship == 'Not-in-family':
                relationship = 1
            elif relationship == 'Own-child':
                relationship = 3
            elif relationship == 'Unmarried':
                relationship = 4
            elif relationship == 'Wife':
                relationship = 5
            else:
                relationship = 2

            race = request.form['race']
            if race == 'White':
                race = 4
            elif race == 'Black':
                race = 2
            elif race == 'Asian-Pac-Islander':
                race = 1
            elif race == 'Amer-Indian-Eskimo':
                race = 0
            else:
                race = 3

            sex = request.form['sex']
            if sex == 'Male':
                sex = 1
            else:
                sex = 0

            hours_per_week = int(request.form['hours_per_week'])


            filename = 'final_model.pickle'
            model = pickle.load(open(filename, 'rb'))

            prediction = model.predict([[age, workclass, education, education_num, marital_status, occupation, relationship, race, sex, hours_per_week]])
            if prediction == 0:
                return 'Your salary is less than 50K'
            else:
                return 'Your salary is greater than 50K'

        except Exception as e:
            print('The Exception message is: ', e)
            return 'something is wrong'

    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True,port=8000)