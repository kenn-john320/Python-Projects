# Lesson Question Answer: 
    # Memes in order of appearance:
    # States of programmer ( Felt like the dog when pwrshell borked on me)
    # Pancake bunny
    # Family Feud + Steve Harvey
    # Capt'n Hook

# Call a commandline tool using subprocess and shlex
# Write a script that calls the "ls" command with "-l"
# argument on a folder. 
# Print the file and the file size of the largest file. 

#!/usr/bin/env bash

import os
import subprocess
import shlex
from subprocess import Popen , PIPE

cmds = "ls -l"

process = subprocess.Popen(shlex.split(cmds), 
        stdout = subprocess.PIPE,
        stderr = subprocess.STDOUT)

for line in iter(process.stdout):
    # print(line)
    splitLine = line.decode().split()
    
    # See what this prints
    # print(splitLine)
    largestFileSize = 0
    currentFileName = ''

    # gets rid of that weird total array thingy
    if len(splitLine) >= 8:
        # print(splitLine)
        fileSize = splitLine[5] 
        fileName = splitLine[9]

        if int(fileSize) >= largestFileSize:
            largestFileSize = fileSize
            currentFileName = fileName
        

print(f'This file is: {currentFileName}')
print(f'This has a file size of : {largestFileSize} bytes! This is the largest.')    