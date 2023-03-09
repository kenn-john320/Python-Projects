#imports libraries
import os
import time
from datetime import datetime, timedelta

# file path
path = 'D:\\Workspace\\Python-Projects\\Comp467\\week3'

#current list of files before going through the loop 
currFiles = os.listdir(path)

start = True
currentTime = datetime.now()
# Will run until False -> Find something new/a change
# Potentially an infinite loop issue 
while start:
    checkFiles = os.listdir(path)
    for file in checkFiles:
        if file not in currFiles:
            print(f'This file: {file} was added at {currentTime}!')
            start = False
        else:
            print(f'Nothing new has been found..')
    time.sleep(1)    

