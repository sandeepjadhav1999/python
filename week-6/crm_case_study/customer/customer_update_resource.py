from flask_restful import Resource
from flask import request
from customer.customer_exceptions import *
from customer.customer_update_service import CustomerUpdate

class CustomerUpdateManipulation(Resource):
    def __init__(self, service: CustomerUpdate) -> None:
        super().__init__()
        self.service = service

    def put(self):
        customer = request.get_json()
        try:
            cnt=self.service.update_customer(customer)
            return {
                'sts': 'success',
                'msg': 'customer updated successfully',
                'res': f'{cnt}'
            }, 201
        except InvalidCustomerMobileException as ex:
            return {
                'sts': 'fail',
                'msg': ex.msg,
                'res': 'Invalid Mobile Number'

            }, 400
        except InvalidCustomerNameException as ex:
            return {
                'sts': 'fail',
                'msg': ex.msg,
                'res': 'Invalid Name'
            }, 400
        except InvalidCustomerDOBException as ex:
            return {
                'sts': 'fail',
                'msg': ex.msg,
                'res': 'Invalid DOB'
            }, 400
        except InvalidCustomerLocException as ex:
            return {
                'sts': 'fail',
                'msg': ex.msg,
                'res': 'Invalid Location'
            }, 400
        except InvalidCustomerStatusException as ex:
            return {
                'sts': 'fail',
                'msg': ex.msg,
                'res': 'Invalid Status'
            }, 400


    