from user_dao import UserDao
from user import User

(message, user)= UserDao.get_one('Diallo123','143')
print(message,user)