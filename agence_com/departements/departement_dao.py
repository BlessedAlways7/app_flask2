import database
from departements.departement import Departement

class DepartementDao:
    connexion = database.connect_db()
    cursor = connexion.cursor()

    def __init__(self) -> None:
        pass

    @classmethod
    def create(cls, dpt:Departement):
        sql = "INSERT INTO departement(nom,emplacement,direction) VALUES(%s,%s,%s)"
        params = (dpt.nom,dpt.emplacement,dpt.direction)
        try:
            DepartementDao.cursor.execute(sql, params)
            DepartementDao.cursor.close()
            message= 'success'
        except Exception as error:
            message = 'failure'
        return message    
        
    
    @classmethod
    def list_all(cls):
        sql = "SELECT * FROM departement"
        try:
            DepartementDao.cursor.execute(sql)
            departements = DepartementDao.cursor.fetchall()
            message = 'success'
        except Exception as error:
            departements = []
            message = "Erreur de récuperation de données! "
        return (message, departements)
    