from pymysql.connections import Connection
from pymysql.cursors import Cursor

from date_util.date_to_json import convert_object_to_dict_which_contains_date
from menu.menu_exception import *
from menu.menu_validation import *

class MenuListService:
    def __init__(self,connection:Connection) -> None:
        self.connection=connection

    def list_all_menu(self)->tuple:
        csr:Cursor=self.connection.cursor()
        self.connection.begin()
        sql:str='select * from menu;'
        csr.execute(sql)
        users:tuple=csr.fetchall()

        users_covert=map(convert_object_to_dict_which_contains_date,users)
        self.connection.commit()
        csr.close()

        return list(users_covert)


    def order_details(self,orderdetails:dict):
        try:
            sts=is_menu_valid(orderdetails)
            if(sts):
                sql='insert into orders(customer_id_mobile,total_quantities,total_price) values (%(customer_id_mobile)s,%(total_quantities)s,%(total_price)s)'
                csr:Cursor=self.connection.cursor()
                self.connection.begin()
                cnt=csr.execute(sql,orderdetails)
                self.connection.commit()
                csr.close()
                return cnt
        except:
            raise
        