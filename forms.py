
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, SelectField, TextAreaField, ValidationError
from wtforms.validators import DataRequired, Email, InputRequired, Optional
from wtforms.fields.core import DateField, RadioField


#FORMS HERE
#FORMS TO BE INCLUDED - USERS, SALESMTPLANNED, SALESMTACTUAL, CUSTOMERS, ... OTHERS?
#////////////////////////////////////////////////////////////
class Login(FlaskForm):
    email = StringField("Enter your email please..", validators=[DataRequired(), Email()]) #Check if true
    password = StringField("Enter your password please..", validators=[DataRequired()])
    submit = SubmitField("For Entering System")


class SalesMTPlanned(FlaskForm): #Will be transformed to a form structure.. check also integer vaidations..
    month_planned = SelectField(label='Month', choices=[("Jan", "Jan"), 
                    ("Feb", "Feb"), ("Mar", "Mar"), ("Apr", "Apr"), ("May", "May"), ("Jun", "Jun")
                    , ("Jul", "Jul"), ("Aug", "Aug"), ("Sep", "Sep"), ("Oct", "Oct"), ("Nov", "Nov")
                    , ("Dec", "Dec") ], validators=[InputRequired()])
    year_planned = IntegerField("Year", validators=[InputRequired()]) #Is integer?1
    #period_planned = StringField("Enter the relevant period please", validators=[DataRequired()])
    tot_vol_planned = IntegerField("Total Sales Volume in MT", validators=[InputRequired()]) #Is integer?
    tot_mf_planned = IntegerField("Total Volume in MT in MF phase", validators=[InputRequired()])
    tot_anodize_planned = IntegerField("Total Volume in MT in ANODIZE phase", validators=[InputRequired()])
    tot_powder_coat_planned = IntegerField("Total Volume in MT in POWDER COATING phase", validators=[InputRequired()])
    tot_wood_finish_planned = IntegerField("Total Volume in MT in WOOD FINISH phase", validators=[InputRequired()])
    tot_crimping_planned = IntegerField("Total Volume in MT in CRIMPING phase", validators=[InputRequired()])
    tot_EUR_planned = IntegerField("Total EUR AMOUNT planned", validators=[InputRequired()])
    new_customers_planned = IntegerField("Total number of new customers planned", validators=[InputRequired()])
    submit = SubmitField("Save This Entry")
    

#////////////////////////////////////////////////////////////
#NEW FORM
class SalesMTActual(FlaskForm): #Will be transformed to a form structure.. check also integer vaidations..
    month_actual = SelectField(label='Month', choices=[("Jan", "Jan"), 
                    ("Feb", "Feb"), ("Mar", "Mar"), ("Apr", "Apr"), ("May", "May"), ("Jun", "Jun")
                    , ("Jul", "Jul"), ("Aug", "Aug"), ("Sep", "Sep"), ("Oct", "Oct"), ("Nov", "Nov")
                    , ("Dec", "Dec") ], validators=[InputRequired()])
    year_actual = IntegerField("Year", validators=[InputRequired()]) #Is integer?1
    #period_actual = StringField("Enter the relevant period please", validators=[DataRequired()])
    tot_vol_actual = IntegerField("Total Sales Volume in MT", validators=[InputRequired()]) #Is integer?
    tot_mf_actual = IntegerField("Total Volume in MT in MF phase", validators=[InputRequired()])
    tot_anodize_actual = IntegerField("Total Volume in MT in ANODIZE phase", validators=[InputRequired()])
    tot_powder_coat_actual = IntegerField("Total Volume in MT in POWDER COATING phase", validators=[InputRequired()])
    tot_wood_finish_actual = IntegerField("Total Volume in MT in WOOD FINISH phase", validators=[InputRequired()])
    tot_crimping_actual = IntegerField("Total Volume in MT in CRIMPING phase", validators=[InputRequired()])
    tot_EUR_actual = IntegerField("Total EUR AMOUNT actual", validators=[InputRequired()])
    new_customers_actual = IntegerField("Total number of new customers actual", validators=[InputRequired()])
    submit = SubmitField("Save This Entry")



#//////////////////////////////////////////////////////////// customer1 form

StringField("Enter your email please..", validators=[DataRequired(), Email()])
IntegerField("Total Volume in MT in MF phase", validators=[InputRequired()])
SelectField(label='Month', choices=[("Jan", "Jan"), 
                    ("Feb", "Feb"), ("Mar", "Mar"), ("Apr", "Apr"), ("May", "May"), ("Jun", "Jun")
                    , ("Jul", "Jul"), ("Aug", "Aug"), ("Sep", "Sep"), ("Oct", "Oct"), ("Nov", "Nov")
                    , ("Dec", "Dec") ], validators=[InputRequired()])
new_date = DateField('DatePicker Test - New', format='%Y-%m-%d')


#Alttakini sileceğiz
def my_length_check(FlaskForm, field):
    if len(field.data) == 0:
        raise ValidationError('This field must be filled in')

"""class MyForm(Form):
    name = StringField('Name', [InputRequired(), my_length_check])"""

class Customer1(FlaskForm):
    
    company_name = StringField("Company Name", validators=[DataRequired()])
    
    staff1_name = StringField("Customer Staff Name-Surname -1", validators=[DataRequired()])
    staff1_birthdate = DateField('Staff 1 Birthdate', format='%Y-%m-%d', validators=[Optional()]) #!!! Optional validator boş bırakabilmemize olanak veriyor.
    staff1_personal_notes = TextAreaField("Personal Notes About Staff -1")
    staff1_email = StringField("Customer Staff E-mail -1", validators=[DataRequired(), Email()])
    
    staff2_name = StringField("Customer Staff Name-Surname -2")
    staff2_birthdate = DateField('Staff 2 Birthdate', format='%Y-%m-%d', validators=[Optional()])
    staff2_personal_notes = TextAreaField("Personal Notes About Staff -2")
    staff2_email = StringField("Customer Staff E-mail -2")

    staff3_name = StringField("Customer Staff Name-Surname -3")
    staff3_birthdate = DateField('Staff 3 Birthdate', format='%Y-%m-%d', validators=[Optional()])
    staff3_personal_notes = TextAreaField("Personal Notes About Staff -3")
    staff3_email = StringField("Customer Staff E-mail -3")
        
    customer_tel1 = StringField("Customer Telephone Number -1")
    customer_tel2 = StringField("Customer Telephone Number -2") 
    customer_tel3 = StringField("Customer Telephone Number -3")
    customer_website = StringField("Customer Website")
    customer_type = SelectField(label='Customer Type', choices=[("Actual", "Actual"), ("Prospect", "Prospect"), ("Suspect", "Suspect")])
    customer_notes = TextAreaField("Notes About Customer/Company")
    local_international  = SelectField(label='Local or International', choices=[("Local", "Local"), ("International", "International"), 
                                    ("Both International and Local", "Both International and Local")])
    customer_country = SelectField(label='Customer Country', choices=[("Turkey", "Turkey"), ("Bulgaria", "Bulgaria"), 
                                    ("Germany", "Germany"), ("Hungary", "Hungary"), ("Other", "Other")])
    customer_address = StringField("Customer Address")
    last_offer_date = DateField('Date of Last Offer Sent to Customer', format='%Y-%m-%d', validators=[Optional()])
    last_offer_result = SelectField(label='Result of Last Offer', choices=[("Accepted", "Accepted"), ("Rejected", "Rejected"), 
                                    ("Pending", "Pending")])
    rejection_reason = StringField("Reason of Rejection - If Rejected")
    customer_source = SelectField(label='How Did Customer Reach Us?', choices=[("Info e-mail/Website", "Info e-mail/Website"), 
                    ("Reference", "Reference"), ("Commercial Fairs", "Commercial Fairs"), ("Social Media", "Social Media"), 
                    ("Other", "Other")])
    reference_name = StringField("Name of Reference - If Any")
    competitor_name = StringField("Name of Competitors the Customer is Buying From - If Any")
    competitor_conditions = StringField("Conditions of Competitors the Customer is Buying From - If Any")
    gender = SelectField(label='Gender of staff 1', choices=[("Male", "Male"), ("Female", "Female"), 
                                    ("Not specified", "Not specified")])
    prefix = SelectField(label='Prefix of Staff -1', choices=[("Mr.", "Mr."), ("Mrs.", "Mrs."), 
                                    ("Ms.", "Ms."), ("Not specified", "Not specified")])
    language1  = StringField("Language Spoken in Company/Country - 1")
    language2  = StringField("Language Spoken in Company/Country - 2")
    language3  = StringField("Language Spoken in Company/Country - 3")
    language4  = StringField("Language Spoken in Company/Country - 4")
    
    submit = SubmitField("Save Customer Information")

    
    #Custom validation does not work??? Check this out
    def validate_companyname(self, company_name):
        if len(company_name.data)==0:
            raise ValidationError('This field must be filled in!!!')
#//////////////////////////////////////////////////////////// end of customer1 form

#//////////////////////////////////////////////////////////// beginning of customer1 search form

class Customer1_Search_Form(FlaskForm):    
    search_company_name = StringField("Please enter the name of the customer to be searched for. You may also enter a part of the customer name. ", validators=[DataRequired()])      
    submit = SubmitField("Search for customer")


#//////////////////////////////////////////////////////////// end of customer1 search form

#////////////////////////////////////////////////////////////

"""#////////////////First example
class MyForm(FlaskForm):
    name = StringField('Name', [InputRequired()])
    def validate_name(form, field):
        if len(field.data) > 50:
            raise ValidationError('Name must be less than 50 characters')
#////////////////Second example
def my_length_check(form, field):
    if len(field.data) > 50:
        raise ValidationError('Field must be less than 50 characters')
class MyForm(Form):
    name = StringField('Name', [InputRequired(), my_length_check])"""


#////////////////////////////////////////////////////////////END-OF FORMS