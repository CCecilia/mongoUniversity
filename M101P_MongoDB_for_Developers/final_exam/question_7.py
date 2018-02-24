import pymongo
from pymongo import MongoClient

connection = MongoClient('localhost', 27017)

db = connection.final_exam

images = db.images.find()

for image in images:
    album_query = {"images": {"$in": [image["_id"]]}}
    album_check = db.albums.find(album_query, {images: 1}).limit(100)
    
    if album_check.count() == 0:
        db.images.delete_one({"_id": image["_id"]});
