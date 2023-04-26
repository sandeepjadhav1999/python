from customer.customer_manipulation_resource import CustomerManipulationResource

from customer.customer_fetch_resource import ListCustomerByAgeResource, ListCustomerByLocationResource
from customer.customer_service import CustomerService
from pymysql.connections import Connection
from customer.customer_update_resource import CustomerUpdateManipulation
from customer.customer_update_service import CustomerUpdate
from customer.customer_block_resource import CustomerBlock
from customer.curtomer_block_service import CustomerBlockSerive
from customer.customer_list_resource import CustomerListResource
from customer.customer_list_serive import CustomerListService

def load_customer_routes(api, connection: Connection):

    service: CustomerService = CustomerService(connection)
    update: CustomerUpdate =CustomerUpdate(connection)
    block:CustomerBlockSerive=CustomerBlockSerive(connection)
    lists:CustomerListService=CustomerListService(connection)


    api.add_resource(
        CustomerManipulationResource,
        '/customer',
        resource_class_kwargs={'service':service}
    )

    api.add_resource(
        ListCustomerByAgeResource,
        '/customer/age/<int:minAge>/<int:maxAge>',
        resource_class_kwargs={'service': service}
    )

    api.add_resource(
        ListCustomerByLocationResource,
        '/customer/location/<string:location>',
        resource_class_kwargs={'service': service}
    )
    api.add_resource(
        CustomerUpdateManipulation,
        '/customer/update',
        resource_class_kwargs={'service':update}
    )
    api.add_resource(
        CustomerBlock,
        '/customer/block',
        resource_class_kwargs={'block':block}
    )
    api.add_resource(
        CustomerListResource,
        '/customer/display',
        resource_class_kwargs={'service':lists}
    )

    