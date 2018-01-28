import pymongo
from pymongo import MongoClient

# connect to DB
connection = MongoClient('localhost', 27017)

db = connection.test

names =  db.names

item = db.names.find_one()

print(item['name'])