from unicodedata import name
from flask import Flask, jsonify,json
from flask_restx import Resource, Api , reqparse

app = Flask(__name__)
api = Api(app)

@api.route('/<name>')
class HelloWorld(Resource):
    def get(self,name):
        
        data=[{
            "name":f"{name}"
        }]
        return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)