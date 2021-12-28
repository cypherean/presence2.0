import pymongo
from datetime import datetime

myclient = pymongo.MongoClient("")

def UpdatePresence(name):
    now = datetime.now()
    dtString = now.strftime("%m-%d-%y %H:%M:%S")
    mydb = myclient["SDSBot"]
    mydb.sdsPresence.find_one_and_update({"Name": name}, {"$set": {"Time": dtString}}, upsert=True)