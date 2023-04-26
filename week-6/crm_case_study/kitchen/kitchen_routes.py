from kitchen.kitechen_manipulation import KitchenManipulationResource
from kitchen.kitchen_service import KitchenService
from pymysql.connections import Connection
from kitchen.kitchen_delete import KitchenDelete
from kitchen.kitchen_delete_service import KitchenDeleteSerive
from kitchen.kitchen_list import KitchenListResource
from kitchen.kitchen_list_service import KitchenListService

def load_kitchen_routes(api, connection: Connection):

    service: KitchenService = KitchenService(connection)
    block:KitchenDeleteSerive=KitchenDeleteSerive(connection)
    lists:KitchenListService=KitchenListService(connection)

    api.add_resource(
        KitchenManipulationResource,
        '/kitchen',
        resource_class_kwargs={'service':service}
    )
    api.add_resource(
        KitchenDelete,
        '/kitchen/delete',
        resource_class_kwargs={'block':block}
    )
    api.add_resource(
        KitchenListResource,
        '/kitchen/display',
        resource_class_kwargs={'service':lists}
    )

