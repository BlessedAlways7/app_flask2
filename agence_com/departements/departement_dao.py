import database
from departements.departement import Departement

class DepartementDao:
    connexion = database.connect_db()
    cursor = connexion.cursor()

  
    @classmethod
    def create(cls, dpt:Departement):
        sql = "INSERT INTO departement (nom,emplacement,direction) VALUES(%s,%s,%s)"
        params = (dpt.nom,dpt.emplacement,dpt.direction)
        try:
            DepartementDao.cursor.execute(sql, params)
            DepartementDao.connexion.commit()
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
    

    @classmethod
    def list_one(cls,nom):
        sql = "SELECT * FROM departement WHERE nom = %s"
        try:
            DepartementDao.cursor.execute(sql,(nom,))
            departement = DepartementDao.cursor.fetchone()
            message = 'success'
        except Exception as error:
            message = 'failure'
            departement = None
        return (message, departement)
    

    @classmethod
    def delete(cls, nom):
        sql = "DELETE FROM departement WHERE nom=%s"
        DepartementDao.cursor.execute(sql, (nom,))
        DepartementDao.connexion.commit()
        DepartementDao.cursor.close()
    

    @classmethod
    def update(cls, dpt:Departement):
        sql = """UPDATE departement SET nom=%s,emplacement=%s,direction=%s, id=%s
                   WHERE 1
              """
        params = (dpt.nom, dpt.emplacement, dpt.direction)
        DepartementDao.cursor.execute(sql, params)
        DepartementDao.connexion.commit() 
        DepartementDao.cursor.close()

        return f"Le département {dpt.direction} est mise à jour avec succès"
