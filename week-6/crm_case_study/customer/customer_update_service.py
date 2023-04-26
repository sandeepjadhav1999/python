import pymysql

from pymysql.connections import Connection
from pymysql.cursors import Cursor

from customer.customer_validations import *

class CustomerUpdate:
    def __init__(self, connection: Connection):
        self.connection = connection

    def update_customer(self, customer: dict) -> int:

        try:
            sts = is_customer_valid(customer)
            if(sts):
                sql = 'update crm_customer set name=%(name)s,email=%(email)s,dob=%(dob)s,location=%(location)s,status=%(status)s where mobile=%(mobile)s'
                csr: Cursor = self.connection.cursor()
                self.connection.begin()
                cnt = csr.execute(sql, customer)
                self.connection.commit()
                csr.close()
                return cnt
        except:
            raise