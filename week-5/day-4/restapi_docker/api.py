from flask import Flask, request
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)


class RestapiDocker(Resource):
    def get (self):
        return {
            'sts':'success',
            'msg':'checking docker setup',
            'res':'your all set'
        }


api.add_resource(RestapiDocker,'/rest')











if __name__ == '__main__':
    app.run(debug=True)