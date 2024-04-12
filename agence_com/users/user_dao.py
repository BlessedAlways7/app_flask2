import database
from users.user import User



class UserDao:
    connexion = database.connect_db()
    cursor = connexion.cursor()


    @classmethod
    def create(cls,user: User):
        sql = "INSERT INTO user (nom_complet,username,password) VALUES (%s,%s,%s)"
        params = (user.nom_complet,user.username,user.password)
        try:
            UserDao.cursor.execute(sql, params)
            UserDao.connexion.commit()
            message = 'success'        
        except Exception as error:
            message = 'failure'
        return message

    @classmethod
    def list_all(cls):
        sql = "SELECT * FROM user"
        try:
            UserDao.cursor.execute(sql)
            users = UserDao.cursor.fetchall()
            message = 'success'
        except Exception as error:
            users = []
            message = 'error'
        return (message, users)
    
    @classmethod
    def get_one(cls,username,password):
        sql = "SELECT * FROM user WHERE username = %s AND password=%s"
        try:
            UserDao.cursor.execute(sql,(username,password))
            user = UserDao.cursor.fetchone()
            message = 'success'
        except Exception as error:
            message = 'failure'
            user =()
            message= user
        return (message, user)
    