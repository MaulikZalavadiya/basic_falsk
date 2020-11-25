from flask import *

app = Flask(__name__)
app.secret_key = 'maulik'


@app.route('/')
def registration():
    return render_template('register.html')


@app.route('/submit',methods=['POST','GET'])
def submit():
    fn_registration = request.form['fn_registration']
    ln_registration = request.form['ln_registration']
    un_registration = request.form['un_registration']
    pwd_registration = request.form['pwd_registration']
    session['fn_registration']=fn_registration
    session['ln_registration'] = ln_registration
    session['un_registration'] = un_registration
    session['pwd_registration'] = pwd_registration

    return render_template('login.html')


@app.route('/login',methods=['POST','GET'])
def login():
    un_login=request.form['un_login']
    pwd_login = request.form['pwd_login']
    session['un_login']=un_login
    session['pwd_login']=pwd_login

    if un_login == session['un_registration'] and pwd_login == session['pwd_registration']:
        return render_template('welcome.html',first_name=session['fn_registration'],last_name=session['ln_registration'])
    else:
        return render_template('login.html' ,error = 'please enter valid username and password.')


@app.route('/submitrefresh')
def subnitrefresh():
    return render_template('login.html', error="")


app.run(debug=True)


#
# from flask import *
#
# app = Flask(__name__)
# app.secret_key = 'maulik'
#
#
# @app.route('/')
# def registration():
#     return render_template('register.html')
#
#
# @app.route('/submit',methods=['POST'])
# def submit():
#     fn_registration = request.form['fn_registration']
#     ln_registration = request.form['ln_registration']
#     un_registration = request.form['un_registration']
#     pwd_registration = request.form['pwd_registration']
#     session['fn_registration']=fn_registration
#     session['ln_registration'] = ln_registration
#     session['un_registration'] = un_registration
#     session['pwd_registration'] = pwd_registration
#
#     return render_template('login.html')
#
#
# @app.route('/login',methods=['POST'])
# def login():
#     un_login=request.form['un_login']
#     pwd_login = request.form['pwd_login']
#     session['un_login']=un_login
#     session['pwd_login']=pwd_login
#
#     if un_login == session['un_registration'] and pwd_login == session['pwd_registration']:
#         return render_template('welcome.html',first_name=session['fn_registration'],last_name=session['ln_registration'])
#     else:
#         return render_template('login.html',erroe='please enter valid username or pass')
#
#
# app.run(debug=True)
#

