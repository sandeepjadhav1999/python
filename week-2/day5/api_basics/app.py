from flask import Flask,jsonify
from typing import Dict
from db.config import Config
import json
app=Flask(__name__)

@app.route('/')
def index():
    return {'info':'this is a jason file'}

@app.route('/demo')
def demo_api():
    dm: Dict = {
        'name': 'abc',
        'is_okay': True,
        'obj': {
            'dt': '2021-01-01'
        },
        'list': [
            {'ttl': 20, 'ip': 'localhost'},
            {'ttl': 10, 'ip': '127.0.0.0'}
        ]
    }

    return dm

@app.route('/config')
def demo_cofig_api():
    cfg=Config()
    return json.dumps(cfg, default=lambda o: vars(o))   
    #default is used as a converter where in the argument o wer are passing  the clg
    # another persentation of lambda :
    #def cl():
        #return vars(o)
     #vars is used to convert a class into dictionary
