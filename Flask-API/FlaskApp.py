from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify

db_connect = create_engine('sqlite:///instances.db')
app = Flask(__name__)
api = Api(app)


class Instances(Resource):
    def get(self):
        conn = db_connect.connect() 
        query = conn.execute("select * from instances") 
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor.fetchall()]}
        return jsonify(result) 

class Instances_Shape(Resource):
    def get(self, Shape):
        conn = db_connect.connect()
        query = conn.execute("select * from instances where Shape =?", (Shape))
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return jsonify(result)


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


api.add_resource(Instances, '/instances', methods = ['GET'])
api.add_resource(Instances_Shape, '/instances/<Shape>', methods = ['GET'])

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')