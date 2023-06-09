from pymysql.connections import Connection
from pymysql.cursors import Cursor

from crm_user.user_exceptions import InActiveUserException, UserNotFoundException


class UserService:
    def __init__(self, connection: Connection) -> None:
        self.connection = connection

    def perform_login(self, mobile: str, password: str) -> dict:
        #cursor is used to write a sql query in python
        csr: Cursor = self.connection.cursor()
        sql = 'select * from crm_user where mobile = %s and password = %s'
        csr.execute(sql, (mobile, password))
        user: dict = csr.fetchone()

        csr.close()

        if(user):
            del user['password']
 
        if not user:
            raise UserNotFoundException('You are entering wrong credentials')
        if user.get('status') == 0:
            raise InActiveUserException('Inactive User, Contact Admin')

        return user