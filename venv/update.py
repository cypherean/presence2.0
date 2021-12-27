import pymongo
from datetime import datetime

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

def UpdatePresence(name):
    now = datetime.now()
    dtString = now.strftime("%H:%M:%S")
    mydb = myclient["test"]
    mydb.sdsPresence.find_one_and_update({"name": name}, {"$set": {"time": dtString}}, upsert=True)