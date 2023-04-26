from pymysql.connections import Connection
from pymysql.cursors import Cursor

class KitchenListService:

    def __init__(self, connection: Connection) -> None:
        self.connection = connection

    def list_all_kitchen(self) -> tuple:
        csr: Cursor = self.connection.cursor()

        self.connection.begin()
        sql: str = 'select * from kitchen'
        csr.execute(sql)
        users: tuple = csr.fetchall()  # tuple of users dictionary which contains date object
        self.connection.commit()
        csr.close()

        return list(users)