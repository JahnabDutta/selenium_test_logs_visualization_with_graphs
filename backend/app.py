from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from db import collection
from datetime import datetime
#import cors
from flask_cors import CORS


app = Flask(__name__)
api = Api(app)
CORS(app)


# api end points-
# # get count of logs based on day
# # get logs filtered by status code
# # get logs filtered by mime type

def get_key_val(doc,key):
    for k,v in doc.items():
        if k == key:
            return v
        elif isinstance(v,dict):
            item = get_key_val(v,key)
            if item is not None:
                return item

    return None


def get_logs_by_day(collection):
    logs_by_day = {}
    for doc in collection.find():
        timestamp = get_key_val(doc,"timestamp")
        if timestamp:
            date = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d')
            if date in logs_by_day:
                logs_by_day[date] += 1
            else:
                logs_by_day[date] = 1
    return logs_by_day


def get_logs_by_key(collection,key):
    logs_by_status= {}
    for doc in collection.find():
        status = get_key_val(doc, key)
        if status:
            if status in logs_by_status:
                timestamp = get_key_val(doc,"timestamp")
                if timestamp:
                    date = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d')
                    if date in logs_by_status[status]:
                        logs_by_status[status][date] += 1
                    else:
                        logs_by_status[status][date] = 1
            else:
                logs_by_status[status] = {}
    return logs_by_status

def equalize_logs(logs_by_key,logs_by_day):
    for key in logs_by_key:
        for day in logs_by_day:
            if day not in logs_by_key[key]:
                logs_by_key[key][day] = 0
    return logs_by_key


    return logs_by_status
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



api.add_resource(GetAllLogs, "/logs/all/")
api.add_resource(GetLogsByStatusCode, "/logs/status/")
api.add_resource(GetLogsByMimeType, "/logs/mime-type/")
api.add_resource(GetLogsBySomeKey, "/logs/<string:key>/")



if __name__ == '__main__':
    app.run(debug=True)