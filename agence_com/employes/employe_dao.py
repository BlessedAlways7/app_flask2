import database
from employes.employe import Employe


class EmployeDao:
    connexion = database.connect_db()
    cursor = connexion.cursor()


    @classmethod
    def create(cls,employe: Employe):
        sql = "INSERT INTO employe (nom,prenom, matricule, fonction, departement) VALUES (%s,%s,%s,%s,%s)"
        params = (employe.nom, employe.prenom,employe.matricule, employe.fonction,employe.departement)
        try:
            EmployeDao.cursor.execute(sql, params)
            EmployeDao.connexion.commit()
            message = 'success'        
        except Exception as error:
            message = 'failure'
        return message

    @classmethod
    def list_all(cls):
        sql = "SELECT * FROM employe"
        try:
            EmployeDao.cursor.execute(sql)
            employes = EmployeDao.cursor.fetchall()
            message = 'success'
        except Exception as error:
            employes = []
            message = 'error'
        return (message, employes)
    

    @classmethod
    def list_one(cls,matricule):
        sql = "SELECT * FROM employe WHERE matricule = %s"
        try:
            EmployeDao.cursor.execute(sql,(matricule,))
            employe = EmployeDao.cursor.fetchone()
            message = 'success'
        except Exception as error:
            message = 'failure'
            employe = None
        return (message, employe)
    
    @classmethod
    def delete(cls, matricule):
        sql = "DELETE FROM employe WHERE matricule=%s"
        EmployeDao.cursor.execute(sql, (matricule,))
        EmployeDao.connexion.commit()
        EmployeDao.cursor.close()

        return f"L'employé de matricule {matricule} est suprimé avec succès"
    
    @classmethod
    def update(cls, emp:Employe):
        sql = """UPDATE employe SET nom=%s,prenom=%s,matricule=%sfonction=%s,departement=%s
                   WHERE id=1
              """
        params = (emp.nom, emp.prenom, emp.matricule, emp.fonction, emp.departement)
        EmployeDao.cursor.execute(sql, params)
        EmployeDao.connexion.commit() 
        EmployeDao.cursor.close()

        return f"L'employé de matricule {emp.matricule} est mise à jour avec succès"

    @classmethod
    def test(cls):
        print('test employeDAO') 

