from pymysql.connections import Connection
from promotion.promotion_resoruce import PromotionResource
from promotion.promotion_service import PromotionListService

def load_promotion_routes(api, connection: Connection):

    service: PromotionListService = PromotionListService(connection)
    
    api.add_resource(
        PromotionResource,
        '/promotion',
        resource_class_kwargs={'service':service}
    )
    