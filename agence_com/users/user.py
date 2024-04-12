class User:
    def __init__(self,nom_complet, username, password) -> None:
        self.__nom_complet = nom_complet
        self.__username = username
        self.__password = password

    @property
    def nom_complet(self):
        return self.__nom_complet

    @nom_complet.setter
    def nom_complet(self, value):
        self.__nom_complet = value

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value

        

  

    