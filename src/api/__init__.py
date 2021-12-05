from flask import jsonify
from flask_restful import Api, Resource
import config


class MessageApi(Resource):
  def get(self):
    return jsonify("hello man")

def crete_apis(app):
  api = Api(app, prefix=config.API_PREFIX)
  api.add_resource(MessageApi, "/message")

