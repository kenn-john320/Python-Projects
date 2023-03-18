import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["KennedyDB"]

mycol = mydb["Students"]

dblist = myclient.list_database_names()
if "KennedyDB" in dblist:
    print("The database exists.")

collist = mydb.list_collection_names()
if "Students" in collist:
    print("The collection exisits.")

mydict = {"Name" : "Steve ", "Major" : "Art History"}

x = mycol.insert_one(mydict)
print(x.inserted_id)