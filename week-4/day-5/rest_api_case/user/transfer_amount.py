from flask import request
from flask_restful import Resource
import json
from pymysql.cursors import Cursor
from pymysql.connections import Connection
from user.transfer_validation import TransferValidation
from user.user_exception import *
from pymysql.err import IntegrityError


class Transfer(Resource):
    def __init__(self,db:Connection):
        self.db=db
        self.validation=TransferValidation()

    def get(self):
        csr: Cursor = self.db.cursor()
        sql = 'select * from account_transactions'
        csr.execute(sql)
        transfer = csr.fetchall()
        csr.close()
        user_str=json.dumps(transfer,sort_keys=True,default=str)
        user_dict=json.loads(user_str)

        return {
            'sts': 'success',
            'msg': 'users in a database',
            'res': user_dict
        }
    
    def post(self):
        transfer=request.get_json()
        try:
            self.validation.is_valid(transfer)
            csr: Cursor = self.db.cursor()
            self.db.begin()
            sql = 'insert into transfer(src_acc,tar_acc,amt) values(%(src_acc)s,%(tar_acc)s,%(amt)s)'
            cnt = csr.execute(sql,transfer)
            self.db.commit()
            csr.close()

            return{
                'sts':'success',
                'msg':'amount transferred',
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

