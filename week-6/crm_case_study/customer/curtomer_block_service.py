from pymysql.connections import Connection
from pymysql.cursors import Cursor
from customer.customer_exceptions import *


class CustomerBlockSerive:

    def __init__(self, connection: Connection) -> None:
        self.connection = connection

    def customer_block(
        self,
        admin_id: str,
        user_id: str,
        status: int
    ) -> bool:

        csr: Cursor = self.connection.cursor()
        self.connection.begin()

        sql = 'select * from crm_customer where mobile = %s'
        csr.execute(sql, (admin_id))
        user: dict = csr.fetchone()

        if(not user):
            raise UserNotFoundException(f'admin {admin_id} not present')

        if user.get('status') != 1:
            raise UnAuthorizedOperationException(
                'only admin can perform activation')

        sql = 'select * from crm_customer where mobile = %s'
        csr.execute(sql, (user_id))

        user: dict = csr.fetchone()
        if(not user):
            raise UserNotFoundException(f'user {user_id} not present')

        if(status == 1 and user.get('status') == 1):
            raise UserAlreadyActivatedException(
                f'{user_id} already activated'
            )

        if(status == 0 and user.get('status') == 0):
            raise UserAlreadyActivatedException(
                f'{user_id} already deactivated'
            )

        sql = 'update crm_customer set status = %s where mobile = %s'
        cnt = csr.execute(sql, (status, user_id))

        self.connection.commit()
        csr.close()

        return cnt