from . import valencia_hospital 
from flask import session, redirect, url_for, render_template, request
from .data import DATA as VALENCIA_DATA
from .data import USERS as VALENCIA_USERS

"""
The Valencia Hospital is developing an application to manage appointments. Design an algorithm for this application with the following features:

It must have a login and validate the data; after the third failed attempt, it should be locked.
The user can schedule an appointment for: General Medicine, Emergency Care, Clinical Analysis, Cardiology, Neurology, Nutrition, Physiotherapy, Traumatology, and Internal Medicine.
There are 3 doctors for each specialty.
The user can only book one appointment per specialist. An error message should be displayed if the user tries to choose two appointments with the same doctor or the same specialty. As a developer, you can choose the doctors' names.
The maximum limit for appointments, in general, is 3.
Upon selecting a specialty, it will display if the user prefers a morning or afternoon appointment and show available hours. As a developer, you can choose the hours.
Display available specialists.
The user can choose their preferred specialist.
The basic process is: Login -> Choose specialty -> Choose doctor -> Choose time slot.
"""
@valencia_hospital.before_request
def before_request_validations():

    if request.endpoint != 'valencia_hospital.login':
        if 'valencia_hospital_login' not in session or not session['valencia_hospital_login']:
            return redirect(url_for('valencia_hospital.login'))


    

@valencia_hospital.route('/')
def hello():
    
    return 'Valencia Hospital'


@valencia_hospital.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'GET':
        return render_template('valencia_hospital/login.html')
        
    if request.method == 'POST':

        if 'valencia_hospital_login_counter' not in session:
            session['valencia_hospital_login_counter'] = 0

        
        session['valencia_hospital_login_counter'] += 1

        user_submitted = request.form.get('valencia_username')
        password_submitted = request.form.get('valencia_password')

        if session['valencia_hospital_login_counter'] > 3:
            error = { 'error': 'too many login attempts' }
            return redirect(url_for('valencia_hospital.hello', **error))
        
        # find and validate user
        matched_user = next((user for user in VALENCIA_USERS['users']\
                            if user['username'] == user_submitted\
                            and user['password'] == password_submitted), None)
        
        print(matched_user)
        print(type(matched_user))

        if matched_user is None:
            print('invalid credentials')
            error = { 'error': 'invalid credentials' }
            return redirect(url_for('valencia_valencia_hospital.hello', **error))
        else:

            session['valencia_hospital_login'] = True
            session['valencia_hospital_login_counter'] = 0

            session['valencia_username'] = user_submitted
            session['valencia_name'] = matched_user['name']
            session['valencia_last_name'] = matched_user['last_name']

            context = {
                'username': session['valencia_username'],
                'name': session['valencia_name'],
                'last_name': session['valencia_last_name'], }
            return redirect(url_for('valencia_hospital.dashboard', **context))
    

@valencia_hospital.route('/dashboard', methods=['GET', 'POST'])
def dashboard():

    specialties = {
        'specialties': [i['name'] for i in VALENCIA_DATA['specialties']]
    }

    if 'appointments' not in session:
        session['appointments'] = []

        return render_template('valencia_hospital/dashboard.html', **specialties)
    
