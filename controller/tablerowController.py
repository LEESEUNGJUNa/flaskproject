from flask_restful import Resource
from flask_restful import reqparse
from service import tablerowService
from flask import jsonify

class Personinfo(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('type', required=True, type=int)
        parser.add_argument('keyword', required=False, type=str)
        parser.add_argument('page', required=False, type=int)
        args = parser.parse_args()
        result = tablerowService.getPersoninfo(args["type"],args["keyword"],args["page"])
        return jsonify(result)

