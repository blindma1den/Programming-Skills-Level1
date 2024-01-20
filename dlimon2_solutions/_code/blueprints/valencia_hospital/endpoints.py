from . import valencia_hospital 
from flask import session, redirect, url_for, render_template, request


@valencia_hospital.before_request
def before_request_validations():

    if 'valencia_hospital_login' not in session\
        or session['valencia_hospital_login'] != True:

        return redirect(url_for('valencia_hospital.login'))
    

@valencia_hospital.route('/')
def hello():
    
    return render_template('valencia_hospital/hello.html')


@valencia_hospital.route('/login', methods=['GET', 'POST'])
def login():

    if 'valencia_hospital_login_counter' not in session:
        session['valencia_hospital_login_counter'] = 0
    
    if request.method == 'GET':
        return render_template('valencia_hospital/login.html')
    
    data = request.form.to_dict()
    session['valencia_hospital_login_counter'] += 1

    if data['valencia_username'] == 'admin' and data['valencia_password'] == 'admin':
        session['valencia_hospital_login'] = True
        return redirect(url_for('valencia_hospital.hello'))
    else:
        return redirect(url_for('valencia_hospital.login'))