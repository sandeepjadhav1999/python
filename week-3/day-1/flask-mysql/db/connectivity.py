import pymysql

class Connectivity:
    def __init__(self):
        self.db=None
        try:
            self.db=pymysql.connect(
                host="localhost",
                user="root",
                password="sandeep",
                database="flaskdb",
                cursorclass=pymysql.cursors.DictCursor
            )
        except:
            print('your credential are wrong')
            db=None