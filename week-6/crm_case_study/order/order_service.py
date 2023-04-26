from pymysql.connections import Connection
from pymysql.cursors import Cursor
from date_util.date_to_json import convert_object_to_dict_which_contains_date

class OrderService:

    def __init__(self, connection: Connection) -> None:
        self.connection = connection

    def list_all_order(self) -> tuple:
        csr: Cursor = self.connection.cursor()

        self.connection.begin()
        sql: str = 'select * from orders'
        csr.execute(sql)
        users: tuple = csr.fetchall()  # tuple of users dictionary which contains date object

        users_convert=map(convert_object_to_dict_which_contains_date,users)
        self.connection.commit()
        csr.close()

        return list(users_convert)