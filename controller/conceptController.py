from flask_restful import Resource
from flask_restful import reqparse
from service import conceptService
from flask import jsonify

class concept(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('keyword', required=True, type=str)
        parser.add_argument('page', required=False, type=int)
        args = parser.parse_args()
        result = conceptService.getconepts(args["keyword"],args["page"])
        return jsonify(result)