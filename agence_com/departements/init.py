from departement_dao import DepartementDao
from departement import Departement



dpt = Departement('Labrie','2eme etage','IT')
data = DepartementDao.create(dpt)
print(data)



(message, departements) = DepartementDao.get_all()
departements= Departement('')
print(message)



