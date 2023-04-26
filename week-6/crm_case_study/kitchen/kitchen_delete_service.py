from pymysql.connections import Connection
from pymysql.cursors import Cursor
from kitchen.kiitechen_exception import *


class KitchenDeleteSerive:

    def __init__(self, connection: Connection) -> None:
        self.connection = connection

    def kitchen_delete(
        self,
        kitchen_id: str,
        name: str
    ) -> bool:

        csr: Cursor = self.connection.cursor()
        self.connection.begin()

        sql = 'select * from kitchen where kitchen_id = %s'
        csr.execute(sql, (kitchen_id))
        user: dict = csr.fetchone()

        if(not user):
            raise IteamNotFoundException(f'iteam id {kitchen_id} not present')

        sql = 'select * from kitchen where name = %s'
        csr.execute(sql, (name))

        user: dict = csr.fetchone()
        if(not user):
            raise IteamNotFoundException(f'dish {name} not present')

        sql = 'delete from kitchen where kitchen_id = %s'
        cnt = csr.execute(sql, kitchen_id)

        self.connection.commit()
        csr.close()

        return cnt