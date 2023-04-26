from flask import request
from flask_restful import Resource
from pymysql.cursors import Cursor
from pymysql.connections import Connection



class Display(Resource):
    def __init__(self,db:Connection):
        self.db=db

    def get(self):
        csr: Cursor = self.db.cursor()
        sql = 'select * from bank_account'
        csr.execute(sql)
        user= csr.fetchall()
        csr.close()
      

        return {
            'sts': 'success',
            'msg': 'users in a database',
            'res': user
        }