from flask_mail import Message,Mail
import MySQLdb
from flask import Flask, render_template, request,redirect, send_from_directory , url_for,session,logging,flash
import pickle
app = Flask(__name__)
import requests
from flask import jsonify
import pandas as pd   
import pdfplumber
import re
import os
import numpy as np
import mysql.connector
import matplotlib
from flask import Flask, Response
import matplotlib.pyplot as plt
matplotlib.use('Agg')
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import io
import base64
UPLOAD_FOLDER = 'python/static'
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import db
app = Flask(__name__, static_folder='static')
app.secret_key = 'mykey'
engine = create_engine('mysql+pymysql://root:new_password@localhost/hirem')
Session = sessionmaker(bind=engine)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:new_password@localhost/hirem'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
db1 = mysql.connector.connect(
    host="localhost",
    user="root",
    password="new_password",
    database="hirem"
)
from models import employee_details 
employees_with_at_least_2_skills = []
criteria_weights = {
    'exp_weight': 0.3,
    'communication_skills_weight': 0.3,
    'time_management_skills_weight': 0.4,
}
db.init_app(app)
def process(input_txt):
    string1 = "give only  the names of the technical skills required for below project(keep it short)"
    string2 = input_txt + string1
    url = "https://open-ai21.p.rapidapi.com/conversationpalm2"
    payload = { "messages": [
		{
			"role": "user",
			"content": string2
		}
	] }
    headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "76f061af65msh092676706989542p17581ajsn3410cc5e8d76",
	"X-RapidAPI-Host": "open-ai21.p.rapidapi.com"
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json().get('BOT')

@app.route('/',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        name = request.form['uname']
        upass = request.form['upass']
        cursor = db1.cursor()
        query = "SELECT * FROM login_cred WHERE uname = %s AND upass = %s"
        cursor.execute(query, (name, upass))
        user = cursor.fetchone()
        if user:
            return render_template('home.html')
        else:
            return render_template('login.html')
    return render_template('login.html')
@app.route('/input',methods=['GET', 'POST'])
def man():
    if request.method == 'POST':
        input_txt = request.form['description']
        output1    = process(input_txt)
        return render_template('requirements.html',ans=output1)
    return render_template('home.html')
@app.route('/input_form',methods=['POST'])
def input_form():
    if request.method == 'POST':
        skill_1 = request.form['skill_1']
        skill_2 = request.form['skill_2']
        skill_3 = request.form['skill_3']
        skill_4 = request.form['skill_4']
        skill_5 = request.form['skill_5']
        skills_from_form = [skill_1, skill_2, skill_3, skill_4, skill_5]
        matched_employees = employee_details.query.filter(
            (employee_details.e_skill_set_1.in_(skills_from_form)) |
            (employee_details.e_skill_set_2.in_(skills_from_form)) |
            (employee_details.e_skill_set_3.in_(skills_from_form)) |
            (employee_details.e_skill_set_4.in_(skills_from_form)) |
            (employee_details.e_skill_set_5.in_(skills_from_form))
        ).all()
        global employees_with_at_least_2_skills 
        employees_with_at_least_2_skills = [
            employee for employee in matched_employees
            if sum(skill in skills_from_form for skill in [
                employee.e_skill_set_1, employee.e_skill_set_2,
                employee.e_skill_set_3, employee.e_skill_set_4, employee.e_skill_set_5
            ]) >= 2
        ]
        return render_template('employee_list.html', employees=employees_with_at_least_2_skills)

def calculate_credit_score(employee):
    exp_worked_weight = criteria_weights['exp_weight']
    communication_skills_weight = criteria_weights['communication_skills_weight']
    time_management_skills_weight = criteria_weights['time_management_skills_weight']
    exp_years = employee.exp_years                                                                    
    communication_skills = employee.communication_skills
    time_management_skills = employee.time_management_skills
    credit_score = (
        exp_years * exp_worked_weight +
        communication_skills * communication_skills_weight +
        time_management_skills * time_management_skills_weight
    )
    return credit_score

@app.route('/second_level',methods=['POST'])
def employees_below_threshold():
    threshold = 2  
    p_th      = 4
    low_credit_score_employees = []
    for employee in employees_with_at_least_2_skills:
        no_of_projects = employee.no_of_projects
        if no_of_projects > p_th:
            continue
        credit_score = calculate_credit_score(employee)
        if credit_score > threshold:
            low_credit_score_employees.append(employee)
    return render_template('employee_list_1.html', employees=low_credit_score_employees)

with open('linear_regression_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/prediction', methods=['POST', 'GET'])
def prediction():
    if request.method == 'POST':
        # Get input values from the form
        Stock_Price = float(request.form['Stock_Price'])
        Profit = float(request.form['Profit'])
        Revenue = float(request.form['Revenue'])
        Budget_Allocation = float(request.form['Budget_Allocation'])
        Market_Demand = request.form['Market_Demand']
        Sales_Forecast = request.form['Sales_Forecast']
        Strategic_Initiatives = request.form['Strategic_Initiatives']
        Employee_Attrition = request.form['Employee_Attrition']
        Workload = request.form['Workload']

        # Preprocess categorical values for prediction
        input_data = pd.DataFrame({
            'Stock_Price': [Stock_Price],
            'Profit': [Profit],
            'Revenue': [Revenue],
            'Budget_Allocation': [Budget_Allocation],
            'Market_Demand': [Market_Demand],
            'Sales_Forecast': [Sales_Forecast],
            'Strategic_Initiatives': [Strategic_Initiatives],
            'Employee_Attrition': [Employee_Attrition],
            'Workload': [Workload]
        })

        prediction = model.predict(input_data)

        return render_template('prediction.html', prediction=int(prediction[0]))
    
    return render_template('prediction.html')
if __name__ == "__main__":
    app.run(debug=True)