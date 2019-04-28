import pymongo

# client = pymongo.MongoClient(host='localhost', port=27017)
client = pymongo.MongoClient('mongodb://192.168.11.138:27017')
db = client.test
collection = db.students

# result = collection.find_one({'name': 'Mike'})
# print(type(result))
# print(result)


# from bson.objectid import ObjectId
#
# result = collection.find_one({'_id': ObjectId("5cc43e059f388c349c2f742d")})
# print(result)


# results = collection.find({'age': 28})
# print(results)
# for result in results:
#     print(result)


# count = collection.count_documents
# print(count)


# condition = {'name': 'Jordan'}
# student = collection.find_one(condition)
# student['age'] = 28
# result = collection.update_one(condition, {'$set': student})
# print(result)
# print(result.matched_count, result.modified_count)


# result = collection.remove({'name': 'Jordan'})
# recomand
#result = collection.delete_one({'name': "Jordan"})
# print(result)


result = collection.delete_one({'name': 'Jordan'})
print(result)
print(result.deleted_count)
results = collection.delete_many({'age': {'$lt': 29}})
print(results.deleted_count)