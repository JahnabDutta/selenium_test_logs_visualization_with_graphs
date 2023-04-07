from flask import Flask, request, jsonify
import json
from flask_restful import Api, Resource
from db import collection
from datetime import datetime
from flask_cors import CORS
from utils import *
import os
from dotenv import load_dotenv

env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path=env_path)

backend_host = os.getenv("BACKEND_HOST")
backend_port = os.getenv("BACKEND_PORT")

app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


# api end points-
# # get count of logs based on day
# # get logs filtered by status code
# # get logs filtered by mime type
# # get logs filtered by some key
# # get raw logs



class GetAllLogs(Resource):
    def get(self):
        logs_by_day = get_logs_by_day(collection)
        return jsonify(logs_by_day)

class GetLogsByStatusCode(Resource):
    def get(self):
        logs_by_status = get_logs_by_key(collection,"status")
        logs_by_status = equalize_logs(logs_by_status,get_logs_by_day(collection))
        return jsonify(logs_by_status)


class GetLogsByMimeType(Resource):
    def get(self):
        logs_by_mime = get_logs_by_key(collection,"mimeType")
        logs_by_mime = equalize_logs(logs_by_mime,get_logs_by_day(collection))
        return jsonify(logs_by_mime)


class GetLogsBySomeKey(Resource):
    def get(self,key):
        logs_by_key = get_logs_by_key(collection,key)
        return jsonify(logs_by_key)


class GetRawLogs(Resource):
    def get(self,value):
        raw_logs = get_raw_logs(collection,value)
        return jsonify(raw_logs)


api.add_resource(GetAllLogs, "/logs/all/")
api.add_resource(GetLogsByStatusCode, "/logs/status/")
api.add_resource(GetLogsByMimeType, "/logs/mime-type/")
api.add_resource(GetLogsBySomeKey, "/logs/<string:key>/")
api.add_resource(GetRawLogs, "/logs/raw/<string:value>/")



if __name__ == '__main__':
    app.run(host = backend_host ,port = backend_port,debug=True)