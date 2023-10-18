from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
db = SQLAlchemy()
class employee_details(db.Model):
    __tablename__ = 'employee_details'
    e_name = db.Column(db.String(80), nullable=False)
    e_exp  = db.Column(db.Integer,nullable=False)
    e_gender = db.Column(db.String(30),nullable=False)
    e_id = db.Column(db.Integer,primary_key=True)
    e_skill_set_1 = db.Column(db.String(30),nullable=False)
    e_skill_set_2  = db.Column(db.String(30),nullable=False)
    e_skill_set_3 = db.Column(db.String(30),nullable=False)
    e_skill_set_4   = db.Column(db.String(30),nullable=False)
    e_skill_set_5 = db.Column(db.String(30),nullable=False,unique=True)
    no_of_projects  = db.Column(db.Integer,nullable=False)
    exp_years       = db.Column(db.Integer,nullable=False)
    communication_skills = db.Column(db.Integer,nullable=False)
    time_management_skills = db.Column(db.Integer,nullable=False)
    