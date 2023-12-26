from flask import Flask, request, render_template
from flask_login import LoginManager 
from psutil import users
from flask_login import LoginManager
from flask import  Flask , render_template,  request
from flask_sqlalchemy import SQLAlchemy
from models import User

app = Flask(__name__)
 
# Create database within app context...
 
with app.app_context():
    

# Tells flask-sqlalchemy what database to connect to
 app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
# Enter a secret key
app.config["SECRET_KEY"] = "ENTER YOUR SECRET KEY"

 # Initialize flask-sqlalchemy extension.
db = SQLAlchemy()
# LoginManager is needed for our application. 
# to be able to log in and out users.
login_manager = LoginManager()
login_manager.init_app(app)

# Creates a user loader callback that returns the user object given an id
@login_manager.user_loader
def loader_user(user_id):
	return User.query.get(user_id)



@app.route('/')
# Home page ...
def route():
 return render_template ('index.html')


# Registration page
@app.route('/form', methods=['POST', 'GET'])
def form():
    if request.method == 'POST':
        username = request.args['username']
        password = request.args['password']
        print(username, password)
        if username in users and users[username]==password:
           return render_template('login')
        else:
           return '<h1> Invalid Credentials </h1>'
    else:
       return render_template("form.html")

    
@app.route('/login')
#Login page
def login():
 return render_template('login.html')

@app.route('/Reviews')
#Review page...
def Reviews():
 return render_template('review.html')

if __name__ == '__main__':
 # Run the flask application on debug mode.....           
 app.run(debug=True)


