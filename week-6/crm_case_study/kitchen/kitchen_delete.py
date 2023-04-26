from flask_restful import Resource
from flask import request
from kitchen.kitchen_delete_service import KitchenDeleteSerive
from customer.customer_exceptions import *

class KitchenDelete(Resource):
    def __init__(self,block:KitchenDeleteSerive):
        self.service=block
    
    def delete(self):
        req_obj: dict = request.get_json()

        try:
            op_res = self.service.kitchen_delete(
                req_obj.get('kitchen_id'),
                req_obj.get('name')
            )

            return {
                'sts': 'success',
                'msg': f"{req_obj.get('name')} deleted successfully",
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