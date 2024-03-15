import pprint
import datetime
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

# Preparation para submit as inf
posts = db.posts

post_id = posts.insert_one(post).inserted_id

print(post_id)

# print(db.posts.find_one())

pprint.pprint(db.posts.find_one())

# bulk insert
new_posts = [{
    "author": "larissa",
    "text": "My life    ",
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
