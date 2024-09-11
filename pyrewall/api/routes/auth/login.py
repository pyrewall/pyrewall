from flask import render_template, request, session, redirect

from pyrewall.core.services.authentication_service import AuthenticationService

from pyrewall.core.dependency_injection import di

from ...application import app

@app.route('/auth/login', methods=['GET'])
def auth_login():
    return render_template('login.html')

@app.route('/auth/login', methods=['POST'])
@di.scoped_inject
def auth_login_post(authentication_service: AuthenticationService):
    username = request.form.get('username')
    password = request.form.get('password')

    user = authentication_service.authenticate_user_with_username_password(username, password)

    if user is None:
        return render_template('login.html')
    
    session['user_id'] = user.id

    return redirect('/')