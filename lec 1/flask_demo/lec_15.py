# task:  fatch data from login html page and print that data another html page
#       login html page is directly run from python file link
# The jinja2 template engine uses the following delimiters for escaping from HTML.
# directive
# {% ... %} for Statements
# {{ ... }} for Expressions to print to the template output
# {# ... #} for Comments not included in the template output
# # ... ## for Line Statements

from flask import *

app = Flask(__name__)


@app.route('/')
def login():
    return render_template('lec15_1.html')


@app.route('/submit', methods=['POST','GET'])
def submit():
    fn = request.form['fn']
    ln = request.form['ln']
    un = request.form['un']
    pwd = request.form['pwd']
    gender = request.form['gender']
    address = request.form['address']
    country = request.form['country']
    h1 = request.form.getlist('hobbies')
    hobbies = '-'.join(h1)

    return render_template('lec15_2.html', first_name=fn, last_name=ln,user_name=un,password=pwd, gender=gender, address=address, country=country,
                           hobbie=hobbies)


app.run(debug=True)
