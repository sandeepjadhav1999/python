from typing import Dict
from flask import Flask,Request
from flask.globals import request
from db.connectivity import Connectivity
from pymysql.cursors import  Cursor
from pymysql.connections import Connection
app=Flask(__name__)


connectivity = Connectivity()
db = connectivity.db


@app.route('/')
def index():

    return {
        'apistatus': True,
        'dbstatus': db is not None,
        'message': 'Database Connectivity and API Integration'
    }


@app.route('/emp', methods=['POST'])
def create_employee():
    emp: dict= request.json
    print(emp)
    csr: Cursor = db.cursor()
    cnt = csr.execute('insert into emp_dt values(%(id)s, %(nm)s)', emp)
    db.commit()
    csr.close()
    return {
        'sts': 'success',
        'msg': 'employee saved successfully',
        'res': cnt
    }

@app.route('/emp')
def all_employees():
    csr: Cursor = db.cursor()
    csr.execute('select * from emp_dt')
    rows = csr.fetchall()
    csr.close()
    return {
        'msg': 'fetched data successfully',
        'status': 'success',
        'res': rows,
        'link':'https://locoalhost:5000/wmp/10'
    },203

@app.route('/emp/<int:id>', methods=['DELETE'])
def delete_employee(id:int):
    csr:Cursor=db.cursor()
    cnt=csr.execute('delete from emp_dt where wmp_dt=%s',(id))
    db.commit()
    csr.close()
    return {
        'msg': 'data deleted successfully',
        'status': 'success',
    }

@app.route('/emp/', methods=['PUT'])
def update_employee():
    '''
        - i need to get data in json from client
        - i need to update new data in database
    '''

    emp: dict = request.json

    csr: Cursor = db.cursor()
    sql = 'update emp_dt set emp_nm = %(nm)s where emp_id = %(id)s'
    csr.execute(sql, emp)

    csr.close()
    db.commit()

    return {
        'sts': 'success',
        'msg':  'data updated successfully',
        'res': 1
    }

@app.route('/emp/<int:id>', methods=['GET'])
def find_emp(id):
    csr=db.cursor()
    cnt=csr.execute('select * from emp_dt where emp_id= %s',(id))
    row=csr.fetchone()
    csr.close()
    return {
        'msg': ' found data successfully',
        'status': 'success',
        "res":row
    }


