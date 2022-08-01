import pymongo

client = pymongo.MongoClient("mongodb+srv://localhost:tonystark123@cluster0.gzbgmji.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name" : "mayurpaunikar",
     "email" : "mayur7@gmail.ai",
     "surname" : "paunikar"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)