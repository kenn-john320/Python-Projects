#Problem: Now that we are part of a studio, we need to modify project 1's script to the
# additional workflows and users on a per work order basis
# • To handle "handoff" we will be using argparse
# • Will also accept AutoDesk Flame files
# • Parse naming of files to put into Database
# • Insert data into Mongo DB
# • Run script 5 separate times to populate data
# • Answer questions with database calls

import argparse
import pymongo
import sys
import os

# Database Schenanigans
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["CurrentDB"]
mycol = mydb["Files"]

dblist = myclient.list_database_names()
if "CurrentDB" in dblist:
    print("The database exists.")

collist = mydb.list_collection_names()
if "Files" in collist:
    print("The collection exists.")


# ArgParse Shenanigans
parser = argparse.ArgumentParser(description="")
parser.add_argument("--files",dest = "files", nargs = '+', help = "")
parser.add_argument("--xytech", help = "")
parser.add_argument("--verbose", action="store_true", help = "Show if Verbose")
parser.add_argument("--output", help = "")
args = parser.parse_args()

print(args.files)

for item in args.files:
    files = open(item,'r').readlines()
    # open multiple files 
    for line in files:
        print(line)


for item in args.xytech:
    




if args.files is None:
    print("No files were selected")
    sys.exit(2)
else: 
    job = args.files