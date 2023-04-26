import pymysql

class Connectivity:
    def __init__(self):
        self.db=None
        try:
            self.db=pymysql.connect(
                host="localhost",
                user="root",
                password="sandeep",
                database="bankcasestudy",
                cursorclass=pymysql.cursors.DictCursor,
                client_flag=pymysql.constants.CLIENT.MULTI_STATEMENTS
            )
        except:
            print('your credential are wrong')
            self.db=None 