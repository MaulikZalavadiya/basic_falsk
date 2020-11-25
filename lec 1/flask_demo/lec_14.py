from flask import Flask,request

app = Flask(__name__)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        fn = request.form['fn']
        ln = request.form['ln']
        gender = request.form['gender']
        address = request.form['address']
        country = request.form['country']
        h1 = request.form.getlist('hobbies')
        hobbie=str('-'.join(h1))
        return '<b>First Name:{}<br> Last name:{}<br> Gender:{}<br> address:{} <br> Country:{}<br>Hobbies:{}</b>'.format(fn,ln,gender,address,country,hobbie)
    else:
        fn = request.args.get('fn')
        ln = request.args.get('ln')
        gender = request.args.get('gender')
        address = request.args.get('address')
        country = request.args.get('country')
        h1 = request.args.getlist('hobbies')
        hobbie = str('-'.join(h1))
        return '<b>First Name:{}<br> Last name:{}<br> Gender:{}<br> address:{} <br>Country:{}<br>Hobbies:{}</b>'.format(fn,ln,gender,address,country,hobbie)

app.run(debug=True)
