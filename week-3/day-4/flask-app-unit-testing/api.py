from flask import Flask
from hello_resource import Hello
from mobile_resource import Mobile


from flask_restful import Api

app = Flask(__name__)
api = Api(app)


api.add_resource(Hello, '/hello')
api.add_resource(Mobile, '/mobile')

if __name__ == '__main__':
    app.run(debug=True)