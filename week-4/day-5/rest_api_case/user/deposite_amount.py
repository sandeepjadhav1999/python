from flask import request
from flask_restful import Resource
import json
from pymysql.cursors import Cursor
from pymysql.connections import Connection
from user.deposite_validation import DepositValidation
from user.user_exception import *
from pymysql.err import IntegrityError


class deposite(Resource):
    def __init__(self,db:Connection):
        self.db=db
        self.validation=DepositValidation()

    def get(self):
        csr: Cursor = self.db.cursor()
        sql = 'select * from account_transactions'
        csr.execute(sql)
        deposites = csr.fetchall()
        csr.close()
        user_str=json.dumps(deposites,sort_keys=True,default=str)
        user_dict=json.loads(user_str)

        return {
            'sts': 'success',
            'msg': 'users in a database',
            'res': user_dict
        }
    
    def post(self):
        deposites=request.get_json()
        try:
            self.validation.is_valid(deposites)
            csr: Cursor = self.db.cursor()
            self.db.begin()
            sql = 'insert into deposit(acc_num_deposit,amt) values(%(acc_num_deposit)s,%(amt)s)'
            cnt = csr.execute(sql,deposites)  
            self.db.commit()
            csr.close()

            return{
                'sts':'success',
                'msg':'amount deposited',
                'res':cnt  
            }
        except IntegrityError as ex:
            return{
                'sts':'fail',
                'msg':'you have given the wrong acc No.'
            },400

        except InvalidAmountException as ex:
            return {
                'sts': 'fail',
                'msg': ex.msg
            }, 400
        except InvalidDetailsException as ex:
            return {
                'sts': 'fail',
                'msg': ex.msg
            }, 400

