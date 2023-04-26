from flask import Flask
from flask_restful import Resource, Api
from flask import CORS


app=Flask(__name__)
CROS(app)

api=Api(app)   #create a new rest api


class Helloworld(Resource):
    def get(self):
        return {
            'sts': 'checking',
            'msg': 'checking flask restful extention',
            'res': 'GET'
        }
    def post(self):
        return {
            'sts': 'checking',
            'msg': 'checking flask restful extention',
            'res': 'POST'
        }

class bye(Resource):
    def get(self):
        return {
            'sts': 'checking',
            'msg': 'checking flask restful extention',
            'res': 'GET'
        }

    def get(self,bye_id):
        return {
            'sts': 'checking',
            'msg': 'checking flask restful extention',
            'res': f'GET {bye_id}'
        }


api.add_resource(Helloworld,'/hello')
api.add_resource(bye,'/bye/<bye_id>')

if __name__=='__main__':
    app.run(debug=True)