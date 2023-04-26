from pymysql.connections import Connection
from menu.menu_resoruce import MenuResource
from menu.menu_service import MenuListService



def load_menu_routes(api, connection: Connection):

    service: MenuListService = MenuListService(connection)
    
    api.add_resource(
        MenuResource,
        '/menu',
        resource_class_kwargs={'service':service}
    )
    