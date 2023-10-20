from flask import Flask, session, request, render_template, redirect, url_for
import bcrypt
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///donnes.db'
app.config['SECRET_KEY'] = "azertyuiopazertyuioazertyuiop"
db = SQLAlchemy(app)

# creation de mon model(user)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

    def __init__(self,email,password,name):
        self.name = name
        self.email = email
        self.password = password

with app.app_context():
    db.create_all()


@app.route('/index')
def index():
    return render_template('/html/index.html')

# creation de la base de donnée de l'utilisateur


@app.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email= request.form['email']
        password = request.form['password']


        new_user =  User(name=name,email=email,password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('/html/register.html')



@app.route('/login',methods=['GET','POST'])
def login():
   
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email, password=password).first()  

        if user:
            birn = User.query.all()
            session['email'] = user.email
            return render_template('/html/dashboard.html',birn=birn)
        else:
            return render_template('/html/login.html',error='ivalid user')
        
    return render_template('/html/login.html')



@app.route('/dashboard')
def dashboard():
    birn = User.query.all()
    if session:
        user = User.query.filter_by(email=session['email']).first()
        return render_template('/html/dashboard.html' ,birn=birn)
    
    return redirect('/logout')


@app.route('/logout')
def logout():
    session.pop('email',None)
    return redirect('/login')



# jai toucher le dashboard et le logout

# @app.route('/dashboard')
# def dashboard():
#     if session['name']:
#         user = User.query.filter_by(email=session['email']).first()
#         return render_template('dashboard.html' ,user=user)
    
#     return redirect('/logout')


# @app.route('/logout')
# def logout():
#     session.pop('email',None)
#     return redirect('/login')
    



if __name__ == '__main__':
    app.run(debug=True)



