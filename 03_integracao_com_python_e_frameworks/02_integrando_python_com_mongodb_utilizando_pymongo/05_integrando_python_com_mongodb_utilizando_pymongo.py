import pprint
import datetime

import pymongo
import pymongo as pyM

client = pyM.MongoClient(
    "mongodb+srv://roberth:123456789abcde@cluster0.avgwvbt.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client.test

collection = db.test_collection

print(db.test_collection)

# Definition the inf from compor o doc

post = {
    "author": "roberth",
    "text": "My first mongoDB application based on python",
    "tags": ["mongodb", "python3", "pymongo"],
    "date": datetime.datetime.utcnow()
}

# Preparation for submit info
posts = db.posts

post_id = posts.insert_one(post).inserted_id

print(post_id)

# print(db.posts.find_one())

pprint.pprint(db.posts.find_one())

# bulk insert
new_posts = [{
    "author": "larissa",
    "text": "My life",
    "tags": ["bulk", "post", "My princess", "insert"],
    "date": datetime.datetime.utcnow()
},
    {
        "author": "gabriel",
        "text": "My soon",
        "title": "history gabriel",
        "date": datetime.datetime(2009, 11, 10, 10, 45)
    }]

result = posts.insert_many(new_posts)
print(result.inserted_ids)

print("\nLast recuperation")
pprint.pprint(db.posts.find_one({"author": "gabriel"}))

print("\nDocument present in collection posts")
for post in posts.find():
    pprint.pprint(post)

posts = db.posts

for post in posts.find():
    pprint.pprint(post)

print("\nCount documents")
print(posts.count_documents({}))

print(posts.count_documents({"author": "larissa"}))

print(posts.count_documents({"tags": "insert"}))

pprint.pprint(posts.find_one({"tags": "insert"}))

print("\n Recuperation collection info in order")
for post in posts.find({}).sort("date"):
    pprint.pprint(post)

result = db.profiles.create_index([('author', pymongo.ASCENDING)], unique=True)

print(sorted(list(db.profiles.index_information())))

user_profile_user = [
    {'user_id': 211, 'name': 'noan'},
    {'user_id': 212, 'name': 'jax'}]

result = db.profile_user.insert_many(user_profile_user)

print("\n Stored collections in MongoDB")
collections = db.list_collection_names()
for collection in collections:
    print(collection)

# db.profiles.drop()

for post in posts.find():
    pprint.pprint(post)

client.drop_database('test')

print(db.list_collection_names())