from flask import Flask,render_template, request

from employes.employe_dao import EmployeDao
from employes.employe import Employe
from departements.departement_dao import DepartementDao
from departements.departement import Departement

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/registrer")
def registrer():
    return render_template("registrer.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/employes")
def employes():
    message, employes = EmployeDao.list_all()
    return render_template("liste_employes.html", message= message, employes= employes)

@app.route('/add-employe', methods= ['POST', 'GET'])
def add_employe():
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
    message, departements = DepartementDao.list_all()
    return render_template("liste_departements.html", message= message, departements= departements)

@app.route('/add-departement', methods= ['POST', 'GET'] )
def add_departement():
    req = request.form
    message =None
    departement=None
    
    if request.method == "POST":
        nom = req ['nom']
        emplacement = req ['emplacement']
        direction = req ['direction']  
        if nom=="" or emplacement=="" or direction=="" :
            message="error"
        else:
            departement = Departement(nom,emplacement, direction)
            message=  DepartementDao.create(departement)
        print(message)
    return render_template('add_departement.html', message = message, departement= departement)

