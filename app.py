from flask_mail import Message,Mail
import MySQLdb
from flask import Flask, render_template, request,redirect, send_from_directory , url_for,session,logging,flash
import pickle
app = Flask(__name__)
import requests
from flask import jsonify
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
db.init_app(app)


def process(input_txt):
    string1 = "give the technical skills required for below project in five lines"
    string2 = input_txt + string1
    url = "https://open-ai21.p.rapidapi.com/conversationgpt35"
    payload = {
	"messages": [
		{
			"role": "user",
			"content": string2
		}
	],
	"web_access": False,
	"stream": False
   }
    headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "0f9ac642acmsh1d46da5f8d12b62p146304jsnc1406de9eae2",
	"X-RapidAPI-Host": "open-ai21.p.rapidapi.com"
   }
    response = requests.post(url, json=payload, headers=headers)
    res = response.json()
    return res.get("BOT")

@app.route('/',methods=['GET', 'POST'])
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
        employees_with_at_least_2_skills = [
            employee for employee in matched_employees
            if sum(skill in skills_from_form for skill in [
                employee.e_skill_set_1, employee.e_skill_set_2,
                employee.e_skill_set_3, employee.e_skill_set_4, employee.e_skill_set_5
            ]) >= 2
        ]
        return render_template('employee_list.html', employees=employees_with_at_least_2_skills)
    
criteria_weights = {
    'hours_worked_weight': 0.3,
    'communication_skills_weight': 0.3,
    'time_management_skills_weight': 0.4,
}
def calculate_credit_score(employee):
    hours_worked_weight = criteria_weights['hours_worked_weight']
    communication_skills_weight = criteria_weights['communication_skills_weight']
    time_management_skills_weight = criteria_weights['time_management_skills_weight']
    hours_worked = employee.hours_worked
    communication_skills = employee.communication_skills
    time_management_skills = employee.time_management_skills
    credit_score = (
        hours_worked * hours_worked_weight +
        communication_skills * communication_skills_weight +
        time_management_skills * time_management_skills_weight
    )
    return credit_score

@app.route('/employees_below_threshold')
def employees_below_threshold():
    # Fetch all employees from the database
    employees = employee_details.query.all()

    # Define the threshold
    threshold = 5  # You can adjust this threshold as needed

    # Calculate the credit scores and filter employees below the threshold
    low_credit_score_employees = []
    for employee in employees:
        credit_score = calculate_credit_score(employee)
        if credit_score < threshold:
            low_credit_score_employees.append((employee, credit_score))

    return render_template('low_credit_score_employees.html', employees=low_credit_score_employees)




if __name__ == '__main__':
    app.run()






if __name__ == "__main__":
    app.run(debug=True)