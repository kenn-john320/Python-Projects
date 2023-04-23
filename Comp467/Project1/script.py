import re
import csv
import numpy as np

# opens text files

xytech = open("xytech.txt", "r")
baselight = open("baselight_export.txt", "r")

# reads each line from the file
xylines = xytech.readlines()
baselines = baselight.readlines()

xyArray = []
baseArray = []

new = []
titleOfgarbage = [] 

# cut the baselight/xytech input by the "/"
for i in range(len(xylines)):
    if re.search("/", xylines[i]):
        # splits the original lines by the / and starts at the 4th word
        # then adds it to the array
        xyArray.append((xylines[i].lstrip(" ").split("/")))      
#print(xyArray)
for i in range(0,5):
    titleOfgarbage.append([xylines[i].lstrip("\n").rstrip("\n")])


for x in range(len(baselines)):
    if re.search("/", baselines[x]):
        #splits original lines by / , removes the \n at the and and starts at the 3rd input
        #then adds it to the array
        baseArray.append(baselines[x].lstrip(" ").strip("\n").split("/"))     
#print(baseArray)


for i in range(len(xylines)):
    for j in range(len(baselines)):
        if re.search("/", xylines[i]):
            x = xylines[i].rstrip("\n").split("/")[3:]
            y = baselines[j].rstrip("\n").split("/")[2:]

            retx = '/'.join(x).rstrip("\n") 
            rety = '/'.join(y).rstrip("\n")
            # print(retx)
            # print(rety)
            if rety.__contains__(retx):
                # take the file path from xytech replace it with baselines
                newString = xylines[i].rstrip("\n").split("/")[1:] + baselines[j].rstrip("\n").split("/")[5:]
                #print(newString)
                new.append('/'.join(newString).rstrip("\n"))
#print(new)

def countNums(_nums): 
    nums = []
    newArr = []

    for x in _nums:
        if x.isnumeric():
            nums.append(int(x))
    #print(nums)
    start = 0
    counter = 1
    end = 0
    for i in range(len(nums)):
            # if array is in a consecutive order
        if start == 0:
            start = nums[i]
        else:
            # check if the next number is the next in succession
            if (start + counter) == nums[i]:

                end = nums[i]
                counter = counter + 1
            else:
                counter = 1
                #print(start)
                if end != 0:
                    newArr.append(f'{start}-{end}')
                else:
                    newArr.append(start)
                    
                start = nums[i]
                end = 0
    #print(start)
    if end != 0:
        newArr.append(f'{start}-{end}')
    else:
        newArr.append(start)
    return newArr

finalGarbage = []

for x in new:
    path, nums = x.split(" ")[0], x.split(" ")[1:]
    #print(nums)
    for group in countNums(nums):
        finalGarbage.append([path, group])

filename = "project1.csv" 

with open("project1.csv", 'w') as csvfile:
    csvwriter = csv.writer(csvfile)

    
    csvwriter.writerows(titleOfgarbage)
    csvwriter.writerows(finalGarbage)




# go line by line in baseline export and replace the folder path with the corresponding one in xytech.txt

# /images1/starwars/reel1/partA/1920x1080 32 33 34 67 68 69 122 123 155 1023 1111 1112 1160 1201 1202 1203 1204 1205 1211 1212 1213 1214
# /hpsans13/production/starwars/reel1/partA/1920x1080
# SWAP FILE PATHS! <Main GOAL>
# Needs to print this:
# /hpsans13/production/starwars/reel1/partA/1920x1080 32 33 34

# Once this is completed, then parse the numbers in the file by its group
# /hpsans13/production/starwars/reel1/partA/1920x1080 32 - 34
# /hpsans13/production/starwars/reel1/partA/1920x1080 67 - 69
# /hpsans13/production/starwars/reel1/partA/1920x1080 122 - 123
# /hpsans13/production/starwars/reel1/partA/1920x1080 155
# /hpsans13/production/starwars/reel1/partA/1920x1080 1023 
