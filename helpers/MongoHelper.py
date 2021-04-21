import pymongo
from pymongo import MongoClient

class MongoHelper:
 
    def __init__(self):
        self.cluster = MongoClient(
    "mongodb+srv://dbUser:1234@cluster0.kihfc.mongodb.net/testDb?retryWrites=true&w=majority")
        self.db = self.cluster['testDb']
        self.mongoCollection = self.db["test"]

    def insert(self,object):
        return self.mongoCollection.insert_one(object)

    def count(self):
        return self.mongoCollection.count_documents({})

    def getAll(self):
        dataList = []
        results = self.mongoCollection.find({})
        for result in results:
            dataList.append(result)
        return dataList
