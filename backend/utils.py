import datetime
import json

def get_key_val(doc,key):
    for k,v in doc.items():
        if k == key:
            return v
        elif isinstance(v,dict):
            item = get_key_val(v,key)
            if item is not None:
                return item
       
    return None

def format_date(date):
    # date is of form "Mon, 03 Apr 2023 14:01:02 GMT"
    day = date.split(" ")[1]
    month = date.split(" ")[2]
    year = date.split(" ")[3]
    return year+"-"+month+"-"+day

def get_logs_by_day(collection):
    logs_by_day = {}
    for doc in collection.find():
        date = get_key_val(doc,"date")
        if date:
            date = format_date(date)
            if date in logs_by_day:
                logs_by_day[date] += 1
            else:
                logs_by_day[date] = 1
    return logs_by_day


def get_logs_by_key(collection,key):
    logs_by_key= {}
    for doc in collection.find():
        key_value = get_key_val(doc, key)
        if key_value:
            if key_value in logs_by_key:
                date = get_key_val(doc,"date")
                if date:
                    date = format_date(date)
                    if date in logs_by_key[key_value]:
                        logs_by_key[key_value][date] += 1
                    else:
                        logs_by_key[key_value][date] = 1
            else:
                logs_by_key[key_value] = {}
    return logs_by_key

def equalize_logs(logs_by_key,logs_by_day):
    for key in logs_by_key:
        for day in logs_by_day:
            if day not in logs_by_key[key]:
                logs_by_key[key][day] = 0
    return logs_by_key


def check_if_contains(doc,value):
    for k,v in doc.items():
        if k == value or v == value:
            return True
        elif isinstance(v,dict):
            if check_if_contains(v,value):
                return True
    return False

def get_raw_logs(collection,value):
    raw_logs = []

    for doc in collection.find():
        contains = check_if_contains(doc,value)
        if(contains):
            doc = doc['message']
            raw_logs.append(json.dumps(doc))
    return raw_logs
