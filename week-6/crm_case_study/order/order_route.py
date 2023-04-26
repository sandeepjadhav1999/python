from pymysql.connections import Connection
from order.order_resource import OrderListResource
from order.order_service import OrderService

def load_Order_routes(api, connection: Connection):
    service: OrderService = OrderService(connection)

    api.add_resource(
        OrderListResource,
        '/order',
        resource_class_kwargs={'service':service}
    )