import re
import csv

# opens text file
xytech = open("xytech.txt", "r")
baselight = open("baselight_export.txt", "r")

xylines = xytech.readlines()
baselines = baselight.readlines()

baseDict = {}

rules = "^[\/\w]*"

# prints each line of the text separeted by the enter
# print(*xylines, sep = "\n")
# print(*baselines, sep = "\n")

# # for every line in the array 
for x in baselines:
   # print(x)

    # see if the line matches the regular expression rule
    result = re.match(rules, x)
    if result:
        if result.group() in baseDict:
            baseDict[result.group()] += x.split(" ")[1:-1:]
        else:
            baseDict[result.group()] = x.split(" ")[1:-1:]
for key in baseDict:
    print(key + " : ")
    print(baseDict[key])
    print("\n")



