from flask import request
from flask_restful import Resource
import json
from pymysql.cursors import Cursor
from pymysql.connections import Connection
from user.activate_validation import ActivateValidation
from user.user_exception import *
from pymysql.err import IntegrityError


class Activate(Resource):
    def __init__(self,db:Connection):
        self.db=db
        self.validation=ActivateValidation()

    def get(self):
        csr: Cursor = self.db.cursor()
        sql = 'select * from bank_account'
        csr.execute(sql)
        users = csr.fetchall()
        csr.close()

        return {
            'sts': 'success',
            'msg': 'users in a database',
            'res': users
        }
    
    def post(self):
        users=request.get_json()
        try:
            self.validation.is_valid(users)
            csr: Cursor = self.db.cursor()
            self.db.begin()
            sql = 'UPDATE bank_account SET ac_sts=(%(ac_sts)s) where ac_num =(%(ac_num)s)'
            cnt = csr.execute(sql,users)
            self.db.commit()
            csr.close()

            return{
                'sts':'success',
                'msg':'account has been activated',
                'res':cnt  
            }
        except IntegrityError as ex:
            return{
                'sts':'fail',
                'msg':'you have given the wrong acc No.'
            },400

        except InvalidStatusException as ex:
            return{
                'sts':'fail',
                'msg':ex.msg
            }
