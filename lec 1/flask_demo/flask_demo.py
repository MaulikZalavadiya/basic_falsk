# from flask import Flask
#
# app=Flask(__name__)
#
# @app.route()
# # app.add_url_rule(‘ / ’, ‘hello’, hello_world)
# def hello_word():
#     return 'hello'
#
# if __name__=='__main__':
#     app.run(host='')


# from flask import Flask
# app = Flask(__name__)
#
# @app.route('/hello/<name>')
# def hello_name(name):
#    return 'Hello %s!' % name
#
# if __name__ == '__main__':
#    app.run(debug = True)


# from flask import Flask
# app = Flask(__name__)
#
# @app.route('/flask')
# def hello_flask():
#    return 'Hello Flask'
#
# @app.route('/python/')
# def hello_python():
#    return 'Hello Python'
#
# if __name__ == '__main__':
#    app.run()

from flask import Flask, redirect, url_for
app = Flask(__name__)

@app.route('/admin')
def hello_admin():
   return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest

@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest',guest = name))

if __name__ == '__main__':
   app.run(debug = True)