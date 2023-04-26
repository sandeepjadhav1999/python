import pymysql

from pymysql.connections import Connection
from pymysql.cursors import Cursor

from kitchen.kitchen_validation import *


# service class will make communication with database
class KitchenService:
    def __init__(self, connection: Connection):
        self.connection = connection

    def save_kitchen(self, kitchen: dict) -> int:

        try:
            sts = is_kitchen_valid(kitchen)
            if(sts):
                sql = 'insert into kitchen(name,price,location) values (%(name)s,%(price)s ,%(location)s)'
                csr: Cursor = self.connection.cursor()
                self.connection.begin()
                cnt = csr.execute(sql, kitchen)
                self.connection.commit()
                csr.close()
                return cnt
        except:
            raise