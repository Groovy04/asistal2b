from bokeh.models.ranges import FactorRange
from flask import Flask, render_template, flash, request, url_for, redirect
from flask_wtf import FlaskForm
from sqlalchemy.orm import session
from wtforms import StringField, SubmitField, IntegerField, SelectField
from wtforms import validators
from wtforms.validators import DataRequired, Email, ValidationError, InputRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date

from flask_login import UserMixin
from flask_login import login_user, current_user, logout_user, login_required

from flask_login import LoginManager
from flask_bcrypt import Bcrypt

#from A_bokeh1 import script, div  #Arrange these in the file


#////////bokeh test libraries
import random
from bokeh.models.tools import Toolbar
import pandas
import numpy as np
import pandas as pd
import pandas

from bokeh.layouts import layout
from bokeh.models.glyphs import Circle
from bokeh.models.sources import ColumnDataSource
from bokeh.plotting import figure, output_file, save
from bokeh.io import curdoc, show
from numpy import source

from bokeh.sampledata.iris import flowers
from bokeh.models import Range1d, PanTool, ResetTool, HoverTool, Band, Toggle, Div
from bokeh.models.annotations import Label, LabelSet, Span, BoxAnnotation, ToolbarPanel
from bokeh.models.widgets import Select, Slider, RadioButtonGroup
from bokeh.layouts import gridplot, row, column
from bokeh.io import curdoc
from bokeh.transform import dodge
from bokeh.resources import CDN
from math import pi

from bokeh.embed import server_document, components

from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import create_engine

from forms import Login, SalesMTPlanned, SalesMTActual, Customer1, Customer1_Search_Form


app = Flask(__name__)

bcrypt = Bcrypt(app)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://tansubaktiran:Avz9p9&9Dgsu_099@193.111.73.99/tansubaktiran"

#Secret key
app.config['SECRET_KEY'] = "$2b$12$P5vdQLFZE.7.Cji.aqKBZOJm8nOL4VT5hP0OWuhHQ216NL5nqAvie"
#Initialize the adatabase
db = SQLAlchemy(app)

#Setting up user login parts
login_manager = LoginManager(app)
login_manager.login_view = 'login' #Name of the route in charge of logging in
login_manager.login_message_category = 'info'


#ADDED FOR TESTING USER LOGIN - 27.10.21
@login_manager.user_loader
def load_user(id):
    return Users_db.query.get(int(id)) #DB table name to be updated!!!! ////////////


#DATABASE MODELS TO BE UPDATED - 
#AUTHORIZED USERS, SALESMTPLANNED, SALESMTACTUAL, CUSTOMERS, ... OTHERS?
class Users_db(db.Model, UserMixin): #TO BE UPDATED!!!
    id = db.Column(db.Integer, primary_key=True)
    name_db = db.Column(db.String(200), nullable=False)
    email_db = db.Column(db.String(120), nullable=False, unique=True)
    password_db = db.Column(db.String(120), nullable=False)
    role_db = db.Column(db.String(20), nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return '<Name %r>' % self.name

#OTHER DATABASES TO BE INCLUDED HERE - 
#//////////////////////////////////////////////////////////// WORKS_DB FOR TEST PURPOSES
#TIME NOW
now = datetime.now()
dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
class Works_db(db.Model): #MT Planned db - 
    id = db.Column(db.Integer, primary_key=True)
    asistal_id_db = db.Column(db.String(20))
    version_db = db.Column(db.Integer)
    date_added_db = db.Column(db.DateTime, default=datetime.utcnow)
    sales_rep_db = db.Column(db.String(50))
    customer_name_db = db.Column(db.String(50))
    customer_drawing_db = db.Column(db.String(50))
    offer_demand_type_db = db.Column(db.String(20))
    mechanical_process_db = db.Column(db.String(20))
    heat_barrier_db = db.Column(db.String(20))
    demand_for_31_certificate_db = db.Column(db.String(20))
    profile_length_db = db.Column(db.Integer, default=0)
    compound_db = db.Column(db.String(10)) #6060, 6063, 6463, 6005, 6061, 6082, 1050,1070
    condition_db = db.Column(db.String(10)) #T4, T5, T6, T64, T66
    surface_db = db.Column(db.String(10)) #Pres, Eloksal, Toz Boya
    additional_equipment_db = db.Column(db.String(10)) #Var, yok
    additional_equipment_explanation_db = db.Column(db.String(300)) #String
    visible_surface_db = db.Column(db.String(10)) #Var, yok - teknik resimde belirtilmeli
    elocsal_coating_thickness_db = db.Column(db.String(10)) #10 microm class, 15 microm class, 20 microm class, 25 microm class, protective(3-5) class
    hanging_print_db = db.Column(db.String(10)) #Var, yok
    hanging_print_explanation_db = db.Column(db.String(300))
    order_amount_in_kg_db = db.Column(db.Integer, default=0)
    profile_section_measure_tolerance_db = db.Column(db.String(30)) #TS EN 755-9, TS EN 12020-2
    order_no_db = db.Column(db.Integer, default=0) #TB String??? or Integer???
    circumference_db = db.Column(db.Integer, default=0)
    area_db = db.Column(db.Integer, default=0)
    weight_in_gr_db = db.Column(db.Integer, default=0)
    press_db = db.Column(db.String(10)) #A,B,D
    difficulty_db = db.Column(db.String(10))

    user1_evaluation_db = db.Column(db.String(20))
    user2_evaluation_db = db.Column(db.String(20))
    user3_evaluation_db = db.Column(db.String(20))
    user4_evaluation_db = db.Column(db.String(20))
    user5_evaluation_db = db.Column(db.String(20))
    user6_evaluation_db = db.Column(db.String(20))
    user7_evaluation_db = db.Column(db.String(20))
    user8_evaluation_db = db.Column(db.String(20))
    user9_evaluation_db = db.Column(db.String(20))
    user10_evaluation_db = db.Column(db.String(20))

    user1_evaluation_explanation_db = db.Column(db.String(400))
    user2_evaluation_explanation_db = db.Column(db.String(400))
    user3_evaluation_explanation_db = db.Column(db.String(400))
    user4_evaluation_explanation_db = db.Column(db.String(400))
    user5_evaluation_explanation_db = db.Column(db.String(400))
    user6_evaluation_explanation_db = db.Column(db.String(400))
    user7_evaluation_explanation_db = db.Column(db.String(400))
    user8_evaluation_explanation_db = db.Column(db.String(400))
    user9_evaluation_explanation_db = db.Column(db.String(400))
    user10_evaluation_explanation_db = db.Column(db.String(400))

    #Her user kendi değerlendirmesini yaptığında log tarih atacak. Buna sonra bakalım.
    user1_evaluation_date_db = db.Column(db.DateTime, default=dt_string)
    user2_evaluation_date_db= db.Column(db.DateTime, default=dt_string)
    user3_evaluation_date_db = db.Column(db.DateTime, default=datetime.utcnow)
    user4_evaluation_date_db = db.Column(db.DateTime, default=datetime.utcnow)
    user5_evaluation_date_db = db.Column(db.DateTime, default=datetime.utcnow)
    user6_evaluation_date_db = db.Column(db.DateTime, default=datetime.utcnow)
    user7_evaluation_date_db = db.Column(db.DateTime, default=datetime.utcnow)
    user8_evaluation_date_db = db.Column(db.DateTime, default=datetime.utcnow)
    user9_evaluation_date_db = db.Column(db.DateTime, default=datetime.utcnow)
    user10_evaluation_date_db = db.Column(db.DateTime, default=datetime.utcnow)
    
        
    def __repr__(self):
        return '<Entry No: %r>' % self.id

#//////////////////////////////////////////////////////////// WORKS_DB FOR TEST PURPOSES






class SALESMTPLANNED_db(db.Model): #MT Planned db - 
    id = db.Column(db.Integer, primary_key=True)
    month_planned_db = db.Column(db.String(15), nullable=False)
    month_order_db = db.Column(db.Integer(), nullable=False, default=0)
    year_planned_db = db.Column(db.Integer(), nullable=False)
    month_unique_db = db.Column(db.String(20), nullable=False)
    tot_vol_planned_db = db.Column(db.Integer, nullable=False, default=0)
    tot_mf_planned_db = db.Column(db.Integer, nullable=False, default=0)
    tot_anodize_planned_db = db.Column(db.Integer, nullable=False, default=0)
    tot_powder_coat_planned_db = db.Column(db.Integer, nullable=False, default=0)
    tot_wood_finish_planned_db = db.Column(db.Integer, nullable=False, default=0)
    tot_crimping_planned_db = db.Column(db.Integer, nullable=False, default=0)
    tot_EUR_planned_db = db.Column(db.Integer, nullable=False, default=0)
    new_customers_planned_db = db.Column(db.Integer, nullable=False, default=0)
    date_added_db = db.Column(db.DateTime, default=datetime.utcnow)
        
    def __repr__(self):
        return '<Entry No: %r>' % self.id

#////////////////////////////////////////////////////////////
#NEW TABLE
class SALESMTACTUAL_db(db.Model): #MT actual db - 
    id = db.Column(db.Integer, primary_key=True)
    month_actual_db = db.Column(db.String(15), nullable=False)
    month_order_db = db.Column(db.Integer(), nullable=False, default=0)
    year_actual_db = db.Column(db.Integer(), nullable=False)
    month_unique_db = db.Column(db.String(20), nullable=False)
    tot_vol_actual_db = db.Column(db.Integer, nullable=False, default=0)
    tot_mf_actual_db = db.Column(db.Integer, nullable=False, default=0)
    tot_anodize_actual_db = db.Column(db.Integer, nullable=False, default=0)
    tot_powder_coat_actual_db = db.Column(db.Integer, nullable=False, default=0)
    tot_wood_finish_actual_db = db.Column(db.Integer, nullable=False, default=0)
    tot_crimping_actual_db = db.Column(db.Integer, nullable=False, default=0)
    tot_EUR_actual_db = db.Column(db.Integer, nullable=False, default=0)
    new_customers_actual_db = db.Column(db.Integer, nullable=False, default=0)
    date_added_db = db.Column(db.DateTime, default=datetime.utcnow)
        
    def __repr__(self):
        return '<Entry No: %r>' % self.id

#NEW TABLE
#////////////////////////////////////////////////////////////
#////////CUSTOMERS DB

class Customer1_db(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name_db = db.Column(db.String(200), nullable=False, unique=True)
    
    staff1_name_db = db.Column(db.String(100), nullable=False)
    staff1_birthdate_db = db.Column(db.DateTime)
    staff1_personal_notes_db = db.Column(db.String(500), nullable=True)
    staff2_name_db = db.Column(db.String(100), nullable=True)
    staff2_birthdate_db = db.Column(db.DateTime) #2021-11-19 00:00:00 ???
    staff2_personal_notes_db = db.Column(db.String(500), nullable=True)
    staff3_name_db = db.Column(db.String(100), nullable=True)
    staff3_birthdate_db = db.Column(db.DateTime)
    staff3_personal_notes_db = db.Column(db.String(500), nullable=True)
    
    staff1_email_db = db.Column(db.String(100), nullable=False)
    staff2_email_db = db.Column(db.String(100), nullable=True)
    staff3_email_db = db.Column(db.String(100), nullable=True)
    customer_tel1_db = db.Column(db.String(50), nullable=True)
    customer_tel2_db = db.Column(db.String(50), nullable=True)
    customer_tel3_db = db.Column(db.String(50), nullable=True)
    customer_website_db = db.Column(db.String(100), nullable=True)
    customer_type_db = db.Column(db.String(50), nullable=True)
    customer_notes_db = db.Column(db.String(500), nullable=True)
    local_international_db = db.Column(db.String(30), nullable=True)
    customer_country_db = db.Column(db.String(50), nullable=True)
    customer_address_db = db.Column(db.String(200), nullable=True)
    last_offer_date_db = db.Column(db.DateTime)
    last_offer_result_db = db.Column(db.String(50), nullable=True)
    rejection_reason_db = db.Column(db.String(100), nullable=True)
    customer_source_db = db.Column(db.String(100), nullable=True)
    reference_name_db = db.Column(db.String(100), nullable=True)
    competitor_name_db = db.Column(db.String(100), nullable=True)
    competitor_conditions_db = db.Column(db.String(500), nullable=True)
    gender_db = db.Column(db.String(20), nullable=True)
    prefix_db = db.Column(db.String(20), nullable=True)
    language1_db = db.Column(db.String(50), nullable=True)
    language2_db = db.Column(db.String(50), nullable=True)
    language3_db = db.Column(db.String(50), nullable=True)
    language4_db = db.Column(db.String(50), nullable=True)
    
def __repr__(self):
        return '<Entry No: %r>' % self.id


#////////endof - CUSTOMERS DB

#ROUTES
@app.route('/')
@app.route('/index')
def index():
    name="TEST"
    number = 10
    return  render_template("index.html", name=name, number=number)


#OTHER ROUTES HERE...
#////////////////////////////////////////////////////////////
@app.route('/sales_planned_entry', methods=["GET", "POST"])
@login_required
def sales_planned_entry(): #Add user - ALSO TO DATABASE!!!
    name = None #For sending to "please enter your name/credentials page on html - if statement"
    form = SalesMTPlanned()
    #Validation of our form
    if form.validate_on_submit():
        #name = form.name_field.data
        #For arranging a code disabling multiple entries for same month/period
        month_unique_temporary = form.month_planned.data + str(form.year_planned.data)
        unique_month = SALESMTPLANNED_db.query.filter_by(month_unique_db=month_unique_temporary).first()
        if unique_month is None:
            #DB MONTH SIRALAMA SCRIPTI. HEMEN ALTINDA DA DATABASE'E ATIYOR.
            month_order ={"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6, "Jul": 7, 
                            "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}
            month_order_no = month_order[form.month_planned.data]
            month_unique = form.month_planned.data + str(form.year_planned.data)
            print(month_unique)
            month = SALESMTPLANNED_db(month_planned_db = form.month_planned.data, 
            month_order_db = month_order_no,
            year_planned_db = form.year_planned.data, 
            month_unique_db = month_unique,
            tot_vol_planned_db = form.tot_vol_planned.data, 
            tot_mf_planned_db = form.tot_mf_planned.data, 
            tot_anodize_planned_db = form.tot_anodize_planned.data, 
            tot_powder_coat_planned_db = form.tot_powder_coat_planned.data, 
            tot_wood_finish_planned_db = form. tot_wood_finish_planned.data, 
            tot_crimping_planned_db = form. tot_crimping_planned.data, tot_EUR_planned_db = form. tot_EUR_planned.data, 
            new_customers_planned_db = form. new_customers_planned.data)
                        
            db.session.add(month)
            db.session.commit()
            flash("Entry recorded successfully! Thank you!", "success")
        #name = form.name_field.data #For sending to "hello -name-"" page on html. Otherwise will keep asking the name/credentials.
        #form.name_field.data = ""
        #form.email_field.data = ""
        else:
            flash("Entry for this month was recorded before! Please update chosen month or choose another month for recording!", 'error')
        
    #User.query.order_by(User.popularity.desc(), User.date_created.desc()).limit(10).all()
    all_records = SALESMTPLANNED_db.query.order_by(SALESMTPLANNED_db.year_planned_db, SALESMTPLANNED_db.month_order_db)
    return  render_template("sales_planned_entry.html", form=form, name=name, all_records=all_records)


#//////////////////////NEW FUNCTION
@app.route('/sales_actual_entry', methods=["GET", "POST"])
@login_required
def sales_actual_entry(): #Add user - ALSO TO DATABASE!!!
    name = None #For sending to "please enter your name/credentials page on html - if statement"
    form = SalesMTActual()
    #Validation of our form
    pending_works = Works_db.query.filter(Works_db.user1_evaluation_db=="Onayla", Works_db.user2_evaluation_db!="Beklemede", Works_db.user3_evaluation_db!="Beklemede", Works_db.user4_evaluation_db!="Beklemede", Works_db.user5_evaluation_db!="Beklemede", 
        Works_db.user6_evaluation_db!="Beklemede", Works_db.user7_evaluation_db!="Beklemede", Works_db.user8_evaluation_db!="Beklemede", Works_db.user9_evaluation_db!="Beklemede", Works_db.user10_evaluation_db!="Beklemede")
    if form.validate_on_submit():
        #name = form.name_field.data
        #For arranging a code disabling multiple entries for same month/period
        month_unique_temporary = form.month_actual.data + str(form.year_actual.data)
        unique_month = SALESMTACTUAL_db.query.filter_by(month_unique_db=month_unique_temporary).first()
        if unique_month is None:
            #DB MONTH SIRALAMA SCRIPTI. HEMEN ALTINDA DA DATABASE'E ATIYOR.
            month_order ={"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6, "Jul": 7, 
                            "Aug": 8, "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12}
            month_order_no = month_order[form.month_actual.data]
            month_unique = form.month_actual.data + str(form.year_actual.data)
            print(month_unique)
            month = SALESMTACTUAL_db(month_actual_db = form.month_actual.data, 
            month_order_db = month_order_no,
            year_actual_db = form.year_actual.data, 
            month_unique_db = month_unique,
            tot_vol_actual_db = form.tot_vol_actual.data, 
            tot_mf_actual_db = form.tot_mf_actual.data, 
            tot_anodize_actual_db = form.tot_anodize_actual.data, 
            tot_powder_coat_actual_db = form.tot_powder_coat_actual.data, 
            tot_wood_finish_actual_db = form. tot_wood_finish_actual.data, 
            tot_crimping_actual_db = form. tot_crimping_actual.data, tot_EUR_actual_db = form. tot_EUR_actual.data, 
            new_customers_actual_db = form. new_customers_actual.data)
                        
            db.session.add(month)
            db.session.commit()
            flash("Entry recorded successfully! Thank you!", "success")
        #name = form.name_field.data #For sending to "hello -name-"" page on html. Otherwise will keep asking the name/credentials.
        #form.name_field.data = ""
        #form.email_field.data = ""
        else:
            flash("Entry for this month was recorded before! Please update chosen month or choose another month for recording!", 'error')
        
    #User.query.order_by(User.popularity.desc(), User.date_created.desc()).limit(10).all()
    all_records = SALESMTACTUAL_db.query.order_by(SALESMTACTUAL_db.year_actual_db, SALESMTACTUAL_db.month_order_db)
    return  render_template("sales_actual_entry.html", form=form, name=name, all_records=all_records)

#//////////////////////NEW FUNCTION

#NEREDE KALDIK? -  AŞAĞIDAKİ UPDATE FONKSİYONUNA TEKRAR BAKILACAK...!
#Update tests-001
@app.route('/update_planned_entry/<int:id>', methods=["GET", "POST"])
@login_required
def update_planned(id):
    #id = None
    form = SalesMTPlanned()
    entry_to_update = SALESMTPLANNED_db.query.get_or_404(id)
    #print(entry_to_update)
    if request.method == "POST": #burayı daha iyi anlamalıyız!!! 
        #- yani eğer update.html üzerinden post edilen bir işlem var ise mi demek istiyor? Buna bakmaya devam...
        print("Yes this is a POST attempt")
        entry_to_update.tot_vol_planned_db = request.form["tot_vol_planned"] #Check here out!! Buraya da bakalım..!!
        entry_to_update.tot_mf_planned_db = request.form["tot_mf_planned"]
        entry_to_update.tot_anodize_planned_db = request.form["tot_anodize_planned"]
        entry_to_update.tot_powder_coat_planned_db = request.form["tot_powder_coat_planned"]
        entry_to_update.tot_wood_finish_planned_db = request.form["tot_wood_finish_planned"]
        entry_to_update.tot_crimping_planned_db = request.form["tot_crimping_planned"]
        entry_to_update.tot_EUR_planned_db = request.form["tot_EUR_planned"]
        entry_to_update.new_customers_planned_db = request.form["new_customers_planned"]
        # Açıklaması için https://stackoverflow.com/questions/10434599/get-the-data-received-in-a-flask-request
        try:
            db.session.commit()
            flash("Your update process is successful", "success")
            all_records = SALESMTPLANNED_db.query.order_by(SALESMTPLANNED_db.year_planned_db, SALESMTPLANNED_db.month_order_db)
            return render_template("update_planned_entry.html", form=form, entry_to_update=entry_to_update, id=id, all_records=all_records)
            
        except:
            db.session.commit()
            flash("Update process failed! Please inform your administrator..", "success")
            all_records = SALESMTPLANNED_db.query.order_by(SALESMTPLANNED_db.year_planned_db, SALESMTPLANNED_db.month_order_db)
            return render_template("update_planned_entry.html", form=form, entry_to_update=entry_to_update, id=id, all_records=all_records)
    else:
        print("NO this is NOT a POST attempt")
        all_records = SALESMTPLANNED_db.query.order_by(SALESMTPLANNED_db.year_planned_db, SALESMTPLANNED_db.month_order_db)
        return render_template("update_planned_entry.html", form=form, entry_to_update=entry_to_update, id=id, all_records=all_records)

#//////////////////////NEW FUNCTION

@app.route('/update_actual_entry/<int:id>', methods=["GET", "POST"])
@login_required
def update_actual(id):
    #id = None
    form = SalesMTActual()
    entry_to_update = SALESMTACTUAL_db.query.get_or_404(id)
    #print(entry_to_update)
    if request.method == "POST": #burayı daha iyi anlamalıyız!!! 
        #- yani eğer update.html üzerinden post edilen bir işlem var ise mi demek istiyor? Buna bakmaya devam...
        print("Yes this is a POST attempt")
        entry_to_update.tot_vol_actual_db = request.form["tot_vol_actual"] #Check here out!! Buraya da bakalım..!!
        entry_to_update.tot_mf_actual_db = request.form["tot_mf_actual"]
        entry_to_update.tot_anodize_actual_db = request.form["tot_anodize_actual"]
        entry_to_update.tot_powder_coat_actual_db = request.form["tot_powder_coat_actual"]
        entry_to_update.tot_wood_finish_actual_db = request.form["tot_wood_finish_actual"]
        entry_to_update.tot_crimping_actual_db = request.form["tot_crimping_actual"]
        entry_to_update.tot_EUR_actual_db = request.form["tot_EUR_actual"]
        entry_to_update.new_customers_actual_db = request.form["new_customers_actual"]
        # Açıklaması için https://stackoverflow.com/questions/10434599/get-the-data-received-in-a-flask-request
        try:
            db.session.commit()
            flash("Your update process is successful", "success")
            all_records = SALESMTACTUAL_db.query.order_by(SALESMTACTUAL_db.year_actual_db, SALESMTACTUAL_db.month_order_db)
            return render_template("update_actual_entry.html", form=form, entry_to_update=entry_to_update, id=id, all_records=all_records)
            
        except:
            db.session.commit()
            flash("Update process failed! Please inform your administrator..", "success")
            all_records = SALESMTACTUAL_db.query.order_by(SALESMTACTUAL_db.year_actual_db, SALESMTACTUAL_db.month_order_db)
            return render_template("update_actual_entry.html", form=form, entry_to_update=entry_to_update, id=id, all_records=all_records)
    else:
        print("NO this is NOT a POST attempt")
        all_records = SALESMTACTUAL_db.query.order_by(SALESMTACTUAL_db.year_actual_db, SALESMTACTUAL_db.month_order_db)
        return render_template("update_actual_entry.html", form=form, entry_to_update=entry_to_update, id=id, all_records=all_records)



#Route for deleting our entries - NEW!! :) PLANNED!!!
@app.route('/delete_planned_entry/<int:id>', methods=["GET", "POST"])
@login_required
def delete_planned(id):
    entry_to_delete = SALESMTPLANNED_db.query.get_or_404(id)
    name = None #For sending to "please enter your name/credentials page on html - if statement"
    form = SalesMTPlanned()
    try:
        db.session.delete(entry_to_delete)
        db.session.commit()
        flash("Entry deleted. Thank you", "success")
        print("Entry deleted.. now should be re-routing to form2??")
        all_records = SALESMTPLANNED_db.query.order_by(SALESMTPLANNED_db.date_added_db)
        return redirect(url_for("sales_planned_entry")) #Orjinal codemy videsounda bu satır yok. 
        # Bunun yerine aşağıdaki satır yazılmış ama delete/n urlinde kalıyordu. 
        # Dolayısı ile sildikten sonra yeni giriş hata veriyordu.
        #return  render_template("form2.html", form=form, name=name, our_users=our_users)
    except:
        flash("There seems to be a problem. Please inform your administrator", 'error')
        return  render_template("sales_planned_entry.html", form=form, name=name, all_records=all_records)


#//////////////////////NEW FUNCTION

#Route for deleting our entries - NEW!! :) ACTUAL!!!
@app.route('/delete_actual_entry/<int:id>', methods=["GET", "POST"])
@login_required
def delete_actual(id):
    entry_to_delete = SALESMTACTUAL_db.query.get_or_404(id)
    #name = None #For sending to "please enter your name/credentials page on html - if statement"
    form = SalesMTActual()
    try:
        db.session.delete(entry_to_delete)
        db.session.commit()
        flash("Entry deleted. Thank you", "success")
        print("Entry deleted.. now should be re-routing to form2??")
        all_records = SALESMTACTUAL_db.query.order_by(SALESMTACTUAL_db.date_added_db)
        return redirect(url_for("sales_actual_entry")) #Orjinal codemy videsounda bu satır yok. 
        # Bunun yerine aşağıdaki satır yazılmış ama delete/n urlinde kalıyordu. 
        # Dolayısı ile sildikten sonra yeni giriş hata veriyordu.
        #return  render_template("form2.html", form=form, name=name, our_users=our_users)
    except:
        flash("There seems to be a problem. Please inform your administrator", 'error')
        return  render_template("sales_actual_entry.html", form=form,  all_records=all_records)

#/////////////////////////////////////////////////////////////////////////////////////////
#///////////////customer_form1
@app.route('/customer_form1', methods=["GET", "POST"])
@login_required
def customer_form1(): #Add user - ALSO TO DATABASE!!!
    name = None #For sending to "please enter your name/credentials page on html - if statement"
    form = Customer1() #Form açılıyor. Kayıt işlemi yapmadık. 18.11.2021! Burada kaldık. Update ve delete işlemleri yapılacak.
    print("Just passed from pre-validate step...")
    #Validation of our form
    unique_company = Customer1_db.query.filter_by(company_name_db=form.company_name).first()
    if form.validate_on_submit():
                
        # POSSIBLY VALIDATORS ARE CONFLICTING WITH SQL REQUIREMENTS.. CHECK ALL 34 FIELDS ONE BY ONE TO SEE THIS...19.11.21
        # SQLALCHEMY NULLABLE DEFAULT GİRİŞLERİNDE SORUN OLDU. AMA ŞİMDİ VERİTABANI KAYIT EDİYOR.
        # UPDATE VE DELETE FONKSİYONLARI YAZILACAK. !!!!! SIRADA BURASI VAR.!!!!!
        # BASİT DE OLSA VERİTABANINDAKİ KAYITLARI LİSTE HALİNDE YAZDIRALIM.
        # HASHING YAZILACAK.
        # DATE KAYITLARINDA TARİH GİRİLMEDİĞİNDE DE NULL OLABİLİYOR MU? BAKALIM.
        # CUSTOMERS TABLE'IN DEVAMINI TANIMLARKEN 1-1 RELATIONSHIP UZERINDEN GIDECEGIZ.
        
        #unique_company = Customer1_db.query.filter_by(company_name_db=form.company_name).first()
        print("Just passed from pre-if step...")
        if unique_company is None:
            print("A unique customer has not been found...")
            
            #Get information from form and make it ready for db recording.
            company = Customer1_db(
            company_name_db=form.company_name.data, 
            staff1_name_db=form.staff1_name.data, 
            staff1_birthdate_db=form.staff1_birthdate.data, 
            staff1_personal_notes_db=form.staff1_personal_notes.data, 
            staff2_name_db=form.staff2_name.data, 
            staff2_birthdate_db=form.staff2_birthdate.data, 
            staff2_personal_notes_db=form.staff2_personal_notes.data, 
            staff3_name_db=form.staff3_name.data, 
            staff3_birthdate_db=form.staff3_birthdate.data, 
            staff3_personal_notes_db=form.staff3_personal_notes.data, 
            staff1_email_db=form.staff1_email.data, 
            staff2_email_db=form.staff2_email.data, 
            staff3_email_db=form.staff3_email.data, 
            customer_tel1_db=form.customer_tel1.data, 
            customer_tel2_db=form.customer_tel2.data, 
            customer_tel3_db=form.customer_tel3.data, 
            customer_website_db=form.customer_website.data, 
            customer_type_db=form.customer_type.data, 
            customer_notes_db=form.customer_notes.data, 
            local_international_db=form.local_international.data, 
            customer_country_db=form.customer_country.data, 
            customer_address_db=form.customer_address.data, 
            last_offer_date_db=form.last_offer_date.data, 
            last_offer_result_db=form.last_offer_result.data, 
            rejection_reason_db=form.rejection_reason.data, 
            customer_source_db=form.customer_source.data, 
            reference_name_db=form.reference_name.data, 
            competitor_name_db=form.competitor_name.data, 
            competitor_conditions_db=form.competitor_conditions.data, 
            gender_db=form.gender.data, 
            prefix_db=form.prefix.data, 
            language1_db=form.language1.data, 
            language2_db=form.language2.data, 
            language3_db=form.language3.data, 
            language4_db=form.language4.data)
            
            
            db.session.add(company)
            
            #BURAYA TEKRAR BAKILACAK - Kaydetmeden(commit öncesi) önce ID lazımsa önce flush, sonra hangi 
            # objeye kaydettiysek (company.id) onun fieldi olarak alabiliyoruz)
            db.session.flush()
            current_id_before_commit = company.id
            new_asistal_ref = "AST" + str(current_id_before_commit)
            print("Just passed from Asistal Ref...//// :", company.id, new_asistal_ref)
            
            #BURAYA TEKRAR BAKILACAK - Yukarıdaki açıklama ile arasındaki kısım

            db.session.commit()
            print("Just passed from post-session step...")
            flash("Entry recorded successfully! Thank you!", "success")
                
    elif unique_company:
            flash("A company with the same name was recorded before! Please update chosen company or enter another company!", 'error')
    
    elif not form.validate_on_submit():
            print("There is a problem in filling the form. Missing field.")
            flash("Please make sure that you have filled 1-Company Name, 2-Customer Staff1 Name and 3- Customer Staff1 E-mail fields.", 'error')
    all_customers = Customer1_db.query.order_by(Customer1_db.id)
    return  render_template("customer_form1.html", form=form, all_customers=all_customers)


#CUSTOMER1 FORM UPDATE - BEGINNING ////////////////////////////////////////////////////////

@app.route('/update_customer1/<int:id>', methods=["GET", "POST"])
@login_required
def update_customer1(id):
    #id = None
    form = Customer1()
    customer_to_update = Customer1_db.query.get_or_404(id)
    #print(entry_to_update)
    
    #Özellikle dropdownların ve textareafield gibi widgetlerin edit/update aşamasında 
    # otomatik olarak doldurulmasını istiyorsak bu hemen aşağıdaki yöntem daha sağlıklı gibi. 
    # Template içindeki value veya default parametreleri çalışmayabiliyor!!! 
    # Tarih/datepicker için de deneyelim.
    if request.method == 'GET':
        form.staff1_personal_notes.data = customer_to_update.staff1_personal_notes_db
        form.gender.data = customer_to_update.gender_db
        form.prefix.data = customer_to_update.prefix_db
        form.staff2_personal_notes.data = customer_to_update.staff2_personal_notes_db
        form.staff3_personal_notes.data = customer_to_update.staff3_personal_notes_db
        
        form.staff1_birthdate.data = customer_to_update.staff1_birthdate_db
        form.staff2_birthdate.data = customer_to_update.staff2_birthdate_db
        form.staff3_birthdate.data = customer_to_update.staff3_birthdate_db

        form.customer_type.data = customer_to_update.customer_type_db
        form.local_international.data = customer_to_update.local_international_db
        
        form.customer_country.data = customer_to_update.customer_country_db    
        form.customer_notes.data = customer_to_update.customer_notes_db
        form.last_offer_date.data = customer_to_update.last_offer_date_db
        form.last_offer_result.data = customer_to_update.last_offer_result_db
        form.rejection_reason.data = customer_to_update.rejection_reason_db
        form.customer_source.data = customer_to_update.customer_source_db

    if request.method == "POST": #burayı daha iyi anlamalıyız!!! 
        #- yani eğer update.html üzerinden post edilen bir işlem var ise mi demek istiyor? Buna bakmaya devam...
        print("Yes this is a POST attempt")
        # Açıklaması için https://stackoverflow.com/questions/10434599/get-the-data-received-in-a-flask-request
        
        customer_to_update.company_name_db=request.form["company_name"]
        customer_to_update.staff1_name_db=request.form["staff1_name"]
        #customer_to_update.staff1_birthdate_db=request.form["staff1_birthdate"]
        
        print("staff 1 birthdate : ", request.form["staff1_birthdate"])
        print("staff 1 birthdate type : ", type(request.form["staff1_birthdate"]))
        if not request.form["staff1_birthdate"]:
            print("staff 1 birthdate check no2: ", request.form["staff1_birthdate"])
            print("birthdate was already None/Null.. so I did not change...")
        #Customer update işleminden sonra girilmemiş datetimelar 00 00 00 formatında kaydoluyor. Önüne geçmeye çalışıyoruz.
            customer_to_update.staff1_birthdate_db=None
        else:
            print("staff 1 birthdate check no else phase: ")
            customer_to_update.staff1_birthdate_db=request.form["staff1_birthdate"]
        #Bu (hemen yukarıdaki) yaklaşım çalıştı gibi görünüyor. Test etmeye devam. Çalıştı ise diğer datetimeler için uygulayalım.. teste devam..!!!26.11.2021

        customer_to_update.staff1_personal_notes_db=request.form["staff1_personal_notes"]
        customer_to_update.staff2_name_db=request.form["staff2_name"]
        
        if not request.form["staff2_birthdate"]:
            customer_to_update.staff2_personal_notes_db=None
        else:
            customer_to_update.staff2_birthdate_db=request.form["staff2_birthdate"]
        
        customer_to_update.staff2_personal_notes_db=request.form["staff2_personal_notes"]
        customer_to_update.staff3_name_db=request.form["staff3_name"]
        
        if not request.form["staff3_birthdate"]:
            customer_to_update.staff3_personal_notes_db=None
        else:
            customer_to_update.staff3_birthdate_db=request.form["staff3_birthdate"]

        customer_to_update.staff3_personal_notes_db=request.form["staff3_personal_notes"]
        customer_to_update.staff1_email_db=request.form["staff1_email"]
        customer_to_update.staff2_email_db=request.form["staff2_email"]
        customer_to_update.staff3_email_db=request.form["staff3_email"]
        customer_to_update.customer_tel1_db=request.form["customer_tel1"]
        customer_to_update.customer_tel2_db=request.form["customer_tel2"]
        customer_to_update.customer_tel3_db=request.form["customer_tel3"]
        customer_to_update.customer_website_db=request.form["customer_website"]
        customer_to_update.customer_type_db=request.form["customer_type"]
        
        customer_to_update.customer_notes_db=request.form["customer_notes"]
        customer_to_update.local_international_db=request.form["local_international"]
        customer_to_update.customer_country_db=request.form["customer_country"]
        customer_to_update.customer_address_db=request.form["customer_address"]
        
        if not request.form["last_offer_date"]:
            customer_to_update.last_offer_date_db=None
        else:
            customer_to_update.last_offer_date_db=request.form["last_offer_date"]

        customer_to_update.last_offer_result_db=request.form["last_offer_result"]
        customer_to_update.rejection_reason_db=request.form["rejection_reason"]
        customer_to_update.customer_source_db=request.form["customer_source"]
        customer_to_update.reference_name_db=request.form["reference_name"]
        customer_to_update.competitor_name_db=request.form["competitor_name"]
        customer_to_update.competitor_conditions_db=request.form["competitor_conditions"]
        customer_to_update.gender_db=request.form["gender"]
        customer_to_update.prefix_db=request.form["prefix"]
        customer_to_update.language1_db=request.form["language1"]
        customer_to_update.language2_db=request.form["language2"]
        customer_to_update.language3_db=request.form["language3"]
        customer_to_update.language4_db=request.form["language4"]
        
        try:
            db.session.commit()
            flash("Customer information updated successfully.", "success")
            return render_template("update_customer1.html", form=form, customer_to_update=customer_to_update, id=id)
            
        except:
            db.session.commit()
            flash("Update process failed! Please inform your administrator..", "success")
            return render_template("update_customer1.html", form=form, customer_to_update=customer_to_update, id=id)
    else:
        print("NO this is NOT a POST attempt")
        return render_template("update_customer1.html", form=form, customer_to_update=customer_to_update, id=id)
#CUSTOMER FORM UPDATE -END ////////////////////////////////////////////////////////


#CUSTOMER SEARCH -BEGINNING ////////////////////////////////////////////////////////
@app.route('/customer_search', methods=["GET", "POST"])
@login_required
def customer_search():
    form = Customer1_Search_Form()
    filtered_companies = None
    if form.validate_on_submit():
        print("Customer search started...")        
        searched_company = form.search_company_name.data
        print("The company we are looking for is..:", searched_company)
        #filtered_records2 = Test_DB.query.filter_by(text1_db=searched_text).all() #Only filter
        #GOOD EXAMPLE BELOW
        #query = DBsession.query(AssetsItem).filter_by(
        #AssetsItem.id > 10,
        #AssetsItem.country = 'England')
        #your_count = query.count()
        #AŞAĞIDAKİ SATIR DOĞRUDAN FİRMA İSMİNİ DOĞRU YAZDIĞIMIZDA ÖNÜMÜZE FİRMA İSMİNİ GETİRMEK İÇİN KULLANILABİLİR. 
        # ALTINDAKİ FORMÜL İSE YAZILAN BİR KISIM TEXT FİRMA İSMİNİN İÇİNDE VAR İSE BU TEXTİN BULUNDUĞU BÜTÜN FİRMALARI GETİRİYOR.
        #filtered_companies = Customer1_db.query.filter_by(company_name_db=searched_company).all() #Filter and order
        #!!!METNİN FİRMA İSMİNDE BULUNDUĞU FİRMALARI GETİRİYOR.
        filtered_companies = Customer1_db.query.filter(Customer1_db.company_name_db.contains(searched_company))
        print(filtered_companies)
        if not filtered_companies:
            flash("Sorry, this customer is not found.", "error")
    #all_records = Test_DB.query.order_by(Test_DB.date_added_db)
    #filtered_records = Test_DB.query.filter_by(text1_db="test").all()
    return  render_template("search_customer1.html", form=form, filtered_companies=filtered_companies)
#CUSTOMER SEARCH -END ////////////////////////////////////////////////////////

#CUSTOMER SHOW SELECTED CUSTOMER -BEGINNING ////////////////////////////////////////////////////////
@app.route('/show_customer/<int:id>', methods=["GET", "POST"])
@login_required
def show_customer(id):
    form = Customer1_Search_Form()
    customer_to_show = Customer1_db.query.get_or_404(id)
    
    staff_1_birthdate=customer_to_show.staff1_birthdate_db
    if customer_to_show.staff1_birthdate_db==None:        
        dt_string_staff_1_birthdate=None    
    else:
        dt_string_staff_1_birthdate = staff_1_birthdate.strftime("%d-%m-%Y")    
    
    staff_2_birthdate=customer_to_show.staff2_birthdate_db
    if customer_to_show.staff2_birthdate_db==None:            
        dt_string_staff_2_birthdate=None    
    else:
        dt_string_staff_2_birthdate = staff_2_birthdate.strftime("%d-%m-%Y")

    staff_3_birthdate=customer_to_show.staff3_birthdate_db
    if customer_to_show.staff3_birthdate_db==None:            
        dt_string_staff_3_birthdate=None    
    else:
        dt_string_staff_3_birthdate = staff_3_birthdate.strftime("%d-%m-%Y")

    last_offer_date=customer_to_show.last_offer_date_db
    if customer_to_show.last_offer_date_db==None:
        dt_string_last_offer_date=None    
    else:
        dt_string_last_offer_date = last_offer_date.strftime("%d-%m-%Y")

    

    return  render_template("show_customer.html", customer_to_show=customer_to_show, form=form, id=id, 
    dt_string_staff_1_birthdate=dt_string_staff_1_birthdate, dt_string_staff_2_birthdate=dt_string_staff_2_birthdate, 
    dt_string_staff_3_birthdate=dt_string_staff_3_birthdate, dt_string_last_offer_date=dt_string_last_offer_date)
#CUSTOMER SHOW SELECTED CUSTOMER -END ////////////////////////////////////////////////////////

#CUSTOMER SHOW ALL -END ////////////////////////////////////////////////////////
#Route for showing all customers - NEW!! :)
@app.route('/all_customers', methods=["GET", "POST"])
@login_required
def all_customers():
    form = Customer1_Search_Form()
    customers_to_show = Customer1_db.query.filter_by().all()
    #print(customers_to_show)

    if request.method == "POST":
    #if method post eklenecek..
    #//////
        customers_to_show = None
        if form.validate_on_submit():
            print("Customer search started...")        
            searched_company = form.search_company_name.data
            print("The company we are looking for is..:", searched_company)
            #filtered_records2 = Test_DB.query.filter_by(text1_db=searched_text).all() #Only filter
            #GOOD EXAMPLE BELOW
            #query = DBsession.query(AssetsItem).filter_by(
            #AssetsItem.id > 10,
            #AssetsItem.country = 'England')
            #your_count = query.count()
            #AŞAĞIDAKİ SATIR DOĞRUDAN FİRMA İSMİNİ DOĞRU YAZDIĞIMIZDA ÖNÜMÜZE FİRMA İSMİNİ GETİRMEK İÇİN KULLANILABİLİR. 
            # ALTINDAKİ FORMÜL İSE YAZILAN BİR KISIM TEXT FİRMA İSMİNİN İÇİNDE VAR İSE BU TEXTİN BULUNDUĞU BÜTÜN FİRMALARI GETİRİYOR.
            #filtered_companies = Customer1_db.query.filter_by(company_name_db=searched_company).all() #Filter and order
            #!!!METNİN FİRMA İSMİNDE BULUNDUĞU FİRMALARI GETİRİYOR.
            customers_to_show = Customer1_db.query.filter(Customer1_db.company_name_db.contains(searched_company))
            print(customers_to_show)
            if not customers_to_show:
                flash("Sorry, this customer is not found.", "error")

    #///////
    return  render_template("all_customers.html", customers_to_show=customers_to_show, form=form)


#CUSTOMER SHOW ALL -BEGINNING ////////////////////////////////////////////////////////


@app.route("/login", methods=['GET', 'POST'])
def login():
    
    #HASHING EKLENECEK!! EKLENDİ, ÇALIŞIYOR.
    
    name=None
    if current_user.is_authenticated:
        print("User is ALREADY LOGGED IN")
        return redirect(url_for('index'))
    form = Login()
    if form.validate_on_submit():
        #????????????????????????????????? test password for oguz@oguz.com - 159oguz78
        # tansu@tansu.com - 1234 / derya@derya.com - 1234
                
        print("Form validated")
        user = Users_db.query.filter_by(email_db=form.email.data).first()
        #Eğer şifre doğru olsa bile aranan user'in emaili yanlış ise hata veriyordu çünkü user objesini bulamadığı için 
        # o userın emailini de bulamıyordu. passsword_db attribute yok diyordu. Bu şekilde if kontrolü ile çalışıyor.
        if user:
            password = user.password_db
            print("passcheck hashed", password)
            #password_check = form.password.data
            password_check = bcrypt.check_password_hash(password, form.password.data)
            print(password_check)
            #print("passcheck", password_check)
        
        #name=form.name.data
        #print(form.email.data)
        if user and password_check:
            print("/////////Found this user and his password is correct!!!////// and hashing technique is used!! ;)")
            login_user(user)
            #name=form.name_field.data
            print("User seems to be logged in beybisi..")
            flash('Login Successful. Have a nice day!!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'error')
    return render_template('login.html', title='Login', form=form, name=name)


@app.route("/logout")
def logout():
    logout_user()
    print("The user should have been LOGGED OUT NOW!!!")
    flash('Logout successful. Thank you for using the system', 'success')
    return redirect(url_for('index'))




@app.route('/performance_graph_2021')
@login_required
def performance_graph_2021():
    #//////////////////////////////
    #//////////////////////////////BOKEH TEST REGION

    # Connecting to MySQL server using mysql-python DBAPI 
    engine = create_engine("mysql+pymysql://tansubaktiran:Avz9p9&9Dgsu_099@193.111.73.99/tansubaktiran")
    dbconnection = engine.connect()

    planned_data = pandas.read_sql("select * from SALESMTPLANNED_db", dbconnection)
    actual_data = pandas.read_sql("select * from SALESMTACTUAL_db", dbconnection)
    myfilter = planned_data["year_planned_db"]==2021
    planned_data.sort_values(by='month_order_db', ascending=True, inplace=True)
    filtered_planned_data = planned_data[myfilter]

    source1 = ColumnDataSource(filtered_planned_data)
    source2 = ColumnDataSource(actual_data)

    circle_size=10
    bar_width=.5

    f = figure(x_range=filtered_planned_data["month_unique_db"], title ="Planned and Actual Total Volume (in MT)")
    f.circle(x="month_unique_db", y="tot_vol_planned_db", size=circle_size, fill_alpha=.4, color="navy", source=source1)
    f.vbar(x="month_unique_db", top="tot_vol_actual_db", width=bar_width, color="orangered", fill_alpha=.4, source=source2)

    f2 = figure(x_range=filtered_planned_data["month_unique_db"], title ="Planned and Actual MF (in MT)")
    f2.circle(x="month_unique_db", y="tot_mf_planned_db", size=circle_size , fill_alpha=.4, color="navy", source=source1)
    f2.vbar(x="month_unique_db", top="tot_mf_actual_db", width=bar_width, color="blue", fill_alpha=.4, source=source2)

    f3 = figure(x_range=filtered_planned_data["month_unique_db"], title ="Planned and Actual ANODIZE (in MT)")
    f3.circle(x="month_unique_db", y="tot_anodize_planned_db", size=circle_size, fill_alpha=.4, color="navy", source=source1)
    f3.vbar(x="month_unique_db", top="tot_anodize_actual_db", width=bar_width, color="gold", fill_alpha=.4, source=source2)

    f4 = figure(x_range=filtered_planned_data["month_unique_db"], title ="Planned and Actual POWDER COATING (in MT)")
    f4.circle(x="month_unique_db", y="tot_powder_coat_planned_db", size=circle_size, fill_alpha=.4, color="navy", source=source1)
    f4.vbar(x="month_unique_db", top="tot_powder_coat_actual_db", width=bar_width, color="purple", fill_alpha=.4, source=source2)

    f5 = figure(x_range=filtered_planned_data["month_unique_db"], title ="Planned and Actual WOOD FINISH (in MT)")
    f5.circle(x="month_unique_db", y="tot_wood_finish_planned_db", size=circle_size, fill_alpha=.4, color="navy", source=source1)
    f5.vbar(x="month_unique_db", top="tot_wood_finish_actual_db", width=bar_width, color="green", fill_alpha=.4, source=source2)

    f6 = figure(x_range=filtered_planned_data["month_unique_db"], title ="Planned and Actual CRIMPING (in MT)")
    f6.circle(x="month_unique_db", y="tot_crimping_planned_db", size=circle_size, fill_alpha=.4, color="navy", source=source1)
    f6.vbar(x="month_unique_db", top="tot_crimping_actual_db", width=bar_width, color="turquoise", fill_alpha=.4, source=source2)

    f7 = figure(x_range=filtered_planned_data["month_unique_db"], title ="Planned and Actual Total Revenues (in EUR)")
    f7.circle(x="month_unique_db", y="tot_EUR_planned_db", size=circle_size, fill_alpha=.4, color="navy", source=source1)
    f7.vbar(x="month_unique_db", top="tot_EUR_actual_db", width=bar_width, color="gold", fill_alpha=.4, source=source2)

    f8 = figure(x_range=filtered_planned_data["month_unique_db"], title ="Number of Planned and Actual New Customers")
    f8.circle(x="month_unique_db", y="new_customers_planned_db", size=circle_size, fill_alpha=.4, color="navy", source=source1)
    f8.vbar(x="month_unique_db", top="new_customers_actual_db", width=bar_width, color="lightblue", fill_alpha=.4, source=source2)

    figure_list = [f,f2,f3,f4,f5,f6,f7,f8]
    for fig in figure_list:
        fig.xaxis.major_label_orientation = pi/4

    lay_out = gridplot([[f,f2,f3], [f4,f5,f6],[f7,f8]],plot_width=400, plot_height=400)
    #show(column(Div(text="<h2>Asistal - CRM Dashboard - Test-1 05.11.21 </h2></br><h3>Year 2021 Records</h3></br><h3>Circles are targets, bars are actual values</h3>"), lay_out))
    #show(f)
    script, div = components(lay_out)
    dbconnection.close()

    #IMPROVE THE ABOVE    
    #//////////////////////////////
    #//////////////////////////////BOKEH TEST REGION

    return  render_template("performance_graph_2021.html", script=script, div=div)

#////////////////graph for 2022

@app.route('/performance_graph_2022')
@login_required
def performance_graph_2022():
    #//////////////////////////////
    #//////////////////////////////BOKEH TEST REGION

    # Connecting to MySQL server using mysql-python DBAPI 
    engine = create_engine("mysql+pymysql://tansubaktiran:Avz9p9&9Dgsu_099@193.111.73.99/tansubaktiran")
    dbconnection = engine.connect()

    planned_data = pandas.read_sql("select * from SALESMTPLANNED_db", dbconnection)
    actual_data = pandas.read_sql("select * from SALESMTACTUAL_db", dbconnection)
    myfilter = planned_data["year_planned_db"]==2022
    planned_data.sort_values(by='month_order_db', ascending=True, inplace=True)
    filtered_planned_data = planned_data[myfilter]

    source1 = ColumnDataSource(filtered_planned_data)
    source2 = ColumnDataSource(actual_data)

    circle_size=10
    bar_width=.5

    f = figure(x_range=filtered_planned_data["month_unique_db"], title ="Planned and Actual Total Volume (in MT)")
    f.circle(x="month_unique_db", y="tot_vol_planned_db", size=circle_size, fill_alpha=.4, color="navy", source=source1)
    f.vbar(x="month_unique_db", top="tot_vol_actual_db", width=bar_width, color="orangered", fill_alpha=.4, source=source2)

    f2 = figure(x_range=filtered_planned_data["month_unique_db"], title ="Planned and Actual MF (in MT)")
    f2.circle(x="month_unique_db", y="tot_mf_planned_db", size=circle_size , fill_alpha=.4, color="navy", source=source1)
    f2.vbar(x="month_unique_db", top="tot_mf_actual_db", width=bar_width, color="blue", fill_alpha=.4, source=source2)

    f3 = figure(x_range=filtered_planned_data["month_unique_db"], title ="Planned and Actual ANODIZE (in MT)")
    f3.circle(x="month_unique_db", y="tot_anodize_planned_db", size=circle_size, fill_alpha=.4, color="navy", source=source1)
    f3.vbar(x="month_unique_db", top="tot_anodize_actual_db", width=bar_width, color="gold", fill_alpha=.4, source=source2)

    f4 = figure(x_range=filtered_planned_data["month_unique_db"], title ="Planned and Actual POWDER COATING (in MT)")
    f4.circle(x="month_unique_db", y="tot_powder_coat_planned_db", size=circle_size, fill_alpha=.4, color="navy", source=source1)
    f4.vbar(x="month_unique_db", top="tot_powder_coat_actual_db", width=bar_width, color="purple", fill_alpha=.4, source=source2)

    f5 = figure(x_range=filtered_planned_data["month_unique_db"], title ="Planned and Actual WOOD FINISH (in MT)")
    f5.circle(x="month_unique_db", y="tot_wood_finish_planned_db", size=circle_size, fill_alpha=.4, color="navy", source=source1)
    f5.vbar(x="month_unique_db", top="tot_wood_finish_actual_db", width=bar_width, color="green", fill_alpha=.4, source=source2)

    f6 = figure(x_range=filtered_planned_data["month_unique_db"], title ="Planned and Actual CRIMPING (in MT)")
    f6.circle(x="month_unique_db", y="tot_crimping_planned_db", size=circle_size, fill_alpha=.4, color="navy", source=source1)
    f6.vbar(x="month_unique_db", top="tot_crimping_actual_db", width=bar_width, color="turquoise", fill_alpha=.4, source=source2)

    f7 = figure(x_range=filtered_planned_data["month_unique_db"], title ="Planned and Actual Total Revenues (in EUR)")
    f7.circle(x="month_unique_db", y="tot_EUR_planned_db", size=circle_size, fill_alpha=.4, color="navy", source=source1)
    f7.vbar(x="month_unique_db", top="tot_EUR_actual_db", width=bar_width, color="gold", fill_alpha=.4, source=source2)

    f8 = figure(x_range=filtered_planned_data["month_unique_db"], title ="Number of Planned and Actual New Customers")
    f8.circle(x="month_unique_db", y="new_customers_planned_db", size=circle_size, fill_alpha=.4, color="navy", source=source1)
    f8.vbar(x="month_unique_db", top="new_customers_actual_db", width=bar_width, color="lightblue", fill_alpha=.4, source=source2)

    figure_list = [f,f2,f3,f4,f5,f6,f7,f8]
    for fig in figure_list:
        fig.xaxis.major_label_orientation = pi/4

    lay_out = gridplot([[f,f2,f3], [f4,f5,f6],[f7,f8]],plot_width=400, plot_height=400)
    #show(column(Div(text="<h2>Asistal - CRM Dashboard - Test-1 05.11.21 </h2></br><h3>Year 2021 Records</h3></br><h3>Circles are targets, bars are actual values</h3>"), lay_out))
    #show(f)
    script, div = components(lay_out)
    dbconnection.close()

    #IMPROVE THE ABOVE    
    #//////////////////////////////
    #//////////////////////////////BOKEH TEST REGION

    return  render_template("performance_graph_2022.html", script=script, div=div)




if __name__ == "__main__":
    app.run(debug=True)
