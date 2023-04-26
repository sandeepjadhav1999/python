from flask import request
from flask_restful import Resource
import json
from pymysql.cursors import Cursor
from pymysql.connections import Connection
from user.withdraw_validation import WithdrawValidation
from user.user_exception import *
from pymysql.err import IntegrityError


class Withdraw(Resource):
    def __init__(self,db:Connection):
        self.db=db
        self.validation=WithdrawValidation()

    def get(self):
        csr: Cursor = self.db.cursor()
        sql = 'select * from account_transactions'
        csr.execute(sql)
        withdraw = csr.fetchall()
        csr.close()
        user_str=json.dumps(withdraw,sort_keys=True,default=str)
        user_dict=json.loads(user_str)

        return {
            'sts': 'success',
            'msg': 'users in a database',
            'res': user_dict
        }
    
    def post(self):
        withdraw=request.get_json()
        try:
            self.validation.is_valid(withdraw)
            csr: Cursor = self.db.cursor()
            self.db.begin()
            sql = 'insert into withdraw(acc_num_withdraw,amt) values(%(acc_num_withdraw)s,%(amt)s)'
            cnt = csr.execute(sql,withdraw)
            self.db.commit()
            csr.close()

            return{
                'sts':'success',
                'msg':'amount withdrawed',
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

