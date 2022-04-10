from flask_restful import Resource
from flask_restful import reqparse
from service import countService

class Person(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('type', required=True, type=int)
        parser.add_argument('value', required=False, type=int)
        args = parser.parse_args()
        result = countService.getPersonCount(args["type"],args["value"])
        return {'count': result}

class Visit(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('type', required=True, type=int)
        parser.add_argument('value', required=False, type=int)
        args = parser.parse_args()
        result = countService.getVisitCount(args["type"],args["value"])
        return {'result': result}
