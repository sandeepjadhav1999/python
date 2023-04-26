from flask_restful import Resource
from flask import request
from customer.curtomer_block_service import CustomerBlockSerive
from customer.customer_exceptions import *

class CustomerBlock(Resource):
    def __init__(self,block:CustomerBlockSerive):
        self.service=block
    
    def put(self):
        req_obj: dict = request.get_json()

        try:
            op_res = self.service.customer_block(
                req_obj.get('admin_id'),
                req_obj.get('user_id'),
                req_obj.get('status')
            )

            return {
                'sts': 'success',
                'msg': f"{req_obj.get('user_id')} activated successfully",
                'res': op_res
            }
        except UnAuthorizedOperationException as ex:
            return {
                'sts': 'unauthorized',
                'msg': ex.msg,
                'res': 'operation failed'
            }, 403
        except UserNotFoundException as ex:
            return {
                'sts': 'fail',
                'msg': ex.msg,
                'res': 'not found'
            }, 404
        except UserAlreadyActivatedException as ex:
            return {
                'sts': 'fail',
                'msg': ex.msg,
                'res': 'already activated'
            }, 400