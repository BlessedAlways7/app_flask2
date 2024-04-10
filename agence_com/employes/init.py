from employe_dao import EmployeDao
from employe import Employe

(message, employes) = EmployeDao.get_all()

employe= Employe('Diallo', 'Amadou', 'AM24242', 'Developpeur web', 'IT')
message = EmployeDao.add(employe)
print (message)


(message,employe) =EmployeDao.get_one('AM24242')
print(message,employe)