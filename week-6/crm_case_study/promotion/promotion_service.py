from pymysql.connections import Connection
from pymysql.cursors import Cursor

from date_util.date_to_json import convert_object_to_dict_which_contains_date
from promotion.promotion_exception import *
from promotion.validation import *

class PromotionListService:
    def __init__(self,connection:Connection) -> None:
        self.connection=connection

    def list_all_promotion(self)->tuple:
        csr:Cursor=self.connection.cursor()
        self.connection.begin()
        sql:str='select * from promotion;'
        csr.execute(sql)
        users:tuple=csr.fetchall()

        users_covert=map(convert_object_to_dict_which_contains_date,users)
        self.connection.commit()
        csr.close()

        return list(users_covert)


    def order_details(self,orderdetails:dict):
        try:
            sts=is_promotion_valid(orderdetails)
            if(sts):
                sql='insert into promotion(promotion_id,title,text,st_dt,end_dt) values (%(promotion_id)s,%(title)s,%(text)s,%(st_dt)s,%(end_dt)s)'
                csr:Cursor=self.connection.cursor()
                self.connection.begin()
                cnt=csr.execute(sql,orderdetails)
                self.connection.commit()
                csr.close()
                return cnt
        except:
            raise
        