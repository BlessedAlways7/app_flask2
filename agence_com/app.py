from flask import Flask,render_template, request, redirect, session, url_for
from flask_bcrypt import Bcrypt

from employes.employe_dao import EmployeDao
from employes.employe import Employe
from departements.departement_dao import DepartementDao
from departements.departement import Departement
from users.user_dao import UserDao
from users.user import User


app = Flask(__name__)
app.secret_key = 'clesecrete'
bcrypt = Bcrypt(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/employes")
def employes():
    if 'username' not in session:
        return redirect(url_for('login'))
    message, employes = EmployeDao.list_all()
    return render_template("liste_employes.html", message= message, employes= employes)

@app.route('/add-employe', methods= ['POST', 'GET'])
def add_employe():
    if 'username' not in session:
        return redirect(url_for('login'))
    req = request.form
    message =None
    employe= None

    if request.method == "POST":
        nom = req ['nom']
        prenom = req ['prenom']
        matricule = req ['matricule']
        fonction = req ['fonction']
        departement = req ['departement']
        if nom=="" or prenom=="" or matricule=="" or fonction=="" or departement=="":
            message="error"
        else:
            employe = Employe(nom,prenom,matricule, fonction, departement)
            message = EmployeDao.create(employe)
        print(message)
    return render_template('add_employe.html', message= message, employe=employe)

@app.route("/departements")
def departements():
    if 'username' not in session:
        return redirect(url_for('login'))
    message, departements = DepartementDao.list_all()
    return render_template("liste_departements.html", message= message, departements= departements)

@app.route('/add-departement', methods= ['POST', 'GET'])
def add_departement():
    if 'username' not in session:
        return redirect(url_for('login'))
    req = request.form
    message =None
    departement=None
    
    if request.method == "POST":
        nom = req ['nom']
        emplacement = req ['emplacement']
        direction = req ['direction']  
        
        if nom=="" or emplacement=="" or direction=="":
            message="error"
        else:
            departement = Departement(nom,emplacement, direction)
            message= DepartementDao.create(departement)
        print(message)
    return render_template('add_departement.html', message = message, departement= departement)

@app.route('/register',methods= ['POST', 'GET'])
def registrer():
    req = request.form
    message =None
    user= None

    if request.method == "POST":
        nom_complet = req ['nom_complet']
        username = req ['username']
        password = req ['password']
        #Hash password
        hashed_password = bcrypt.generate_password_hash(password)
        #print('hasshed_password:', hashed_password)
        
        if nom_complet=="" or username=="" or password=="" :
            message="error"
        else:
            user = User(nom_complet, username, hashed_password)
            message = UserDao.create(user)
        print(message)
    return render_template('register.html', message=message, user=user)

@app.route('/login',methods= ['POST', 'GET'])
def login():
    req = request.form
    message =None
    user = None
    if request.method == "POST":
        username = req ['username']
        password = req ['password']     
        if username=="" or password=="":
            message="error"
        else:
            # check password
            (message,user) = UserDao.get_one(username, password)
            
            if message =='success' and user != None: # None ==> Null
                session['nom_complet']=user[1] #On met le nom complet dans notre variable de session
                session['username']=user[2] # On met le username dans notre variable de session
                return redirect(url_for("home"))    
    return render_template('login.html', message=message, user=None)

@app.route("/logout")
def logout():
    session.clear() # On vide la session
    return redirect(url_for('login'))

