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
import pprint as pp
import os
import csv

# Database Schenanigans
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["CurrentDB"]

# First collection list
files_coll = mydb["Files"]
# Second collection list
frames_coll = mydb["Frames"]

# ArgParse Shenanigans
parser = argparse.ArgumentParser(description="")
parser.add_argument("--files",dest = "files", nargs = '+', help = "For Baselight/Flames text files")
parser.add_argument("--xytech", dest = "xytech", help = "For Xytech file input")
parser.add_argument("--verbose", action="store_true", help = "Show if Verbose")
parser.add_argument("--output", help = "Print the output to a CSV or the Database")
args = parser.parse_args()

# print(args.files)

## ~~~  FOR REGULAR FILES  ~~
for item in args.files:
    file_parse = item.split("_")
    files_coll.insert_many([{"Machine Name": file_parse[0], "Name of the User": file_parse[1], "Date of File": file_parse[2].removesuffix('.txt')}])
    #pp.pprint(list(files_coll.find({})))


    files = open(item,'r').readlines()
    # open multiple files 
    for line in files:
        line_parse = line.split(" ")
        # Adds format to database 
        # frames_coll.insert_many([{"Location": line_parse[0], "Frames":line_parse[1:]}])
        #pp.pprint(list(frames_coll.find({})))

if args.files is None:
    print("No files were selected")
    sys.exit(2)
else: 
    job = args.files


# ~~~~~~~~~~~~~~ Project 1 BS ~~~~~~~~~~~

sortedFiles = []

for item in args.files:
    read_baselight_file = open(item, "r")

    xytech_folders = []

    read_xytech_file = open(args.xytech, "r")
    for line in read_xytech_file:
        if "/" in line:
            xytech_folders.append(line) 

#Read each line from Baselight file
    for line in read_baselight_file:

        # GRABS THAT NET FLAME WITH THE SPACE CAUSE CHAJA IS A TROLL 
        line_parse = line.replace("/net/flame-archive", "").split(" ")
        current_folder = line_parse.pop(0)
        sub_folder = current_folder.replace("/images1/Avatar/", "")
        new_location = ""
        #Folder replace check
        for xytech_line in xytech_folders:
            if sub_folder in xytech_line:
                new_location = xytech_line.strip()
        first=""
        pointer=""
        last=""
        for numeral in line_parse:
            #Skip <err> and <null>
            if not numeral.strip().isnumeric():
                continue
            #Assign first number
            if first == "":
                first = int(numeral)
                pointer = first
                continue
            #Keeping to range if succession
            if int(numeral) == (pointer+1):
                pointer = int(numeral)
                continue
            else:
                #Range ends or no sucession, output
                last = pointer
                if first == last:
                    sortedFiles.append([new_location, first])
                    frames_coll.insert_many([{"Location": new_location, "Frames": first, "Date of File": file_parse[2].removesuffix('.txt'), "Name of the User": file_parse[1], "Machine Name": file_parse[0]} ])
                    # sortedFiles.append("%s %s" % (new_location, first))
                else:
                    sortedFiles.append([new_location, f"{first} - {last}"])
                    frames_coll.insert_many([{"Location": new_location, "Frames": f"{first} - {last}", "Date of File": file_parse[2].removesuffix('.txt'), "Name of the User": file_parse[1], "Machine Name": file_parse[0]}])
                    #sortedFiles.append("%s %s-%s" % (new_location, first, last))
                first= int(numeral)
                pointer=first
                last=""
        #Working with last number each line 
        last = pointer
        if first != "":
            if first == last:
                sortedFiles.append([new_location, first])
                frames_coll.insert_many([{"Location": new_location, "Frames": first, "Date of File": file_parse[2].removesuffix('.txt'), "Name of the User": file_parse[1], "Machine Name": file_parse[0]}])
                #sortedFiles.append("%s %s" % (new_location, first))
            else:
                sortedFiles.append([new_location, f"{first} - {last}"])
                frames_coll.insert_many([{"Location": new_location, "Frames": f"{first} - {last}", "Date of File": file_parse[2].removesuffix('.txt'), "Name of the User": file_parse[1], "Machine Name": file_parse[0]}])
                #sortedFiles.append("%s %s-%s" % (new_location, first, last))

# print(sortedFiles)
# for row in sortedFiles:
#     print(row)

## ~~ FOR XYTECH FILES
if args.xytech is None:
    print("No files were selected")
    sys.exit(2)
else: 
    job = args.xytech


# ~~ FOR 
if args.verbose:
    print(f'The args file(s): {args.files} and the args.xytech file(s): {args.xytech} are verbose! ' )


filename = "Project2.csv"

with open(filename, "w+") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(sortedFiles)


