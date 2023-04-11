# Create an Argparse script
# Add arguments for importing any text file and a "verbose" option 
# that prints each line if that option is flagged. 
# Print the total lines from that file at the end of script​
# Submit the code and output from running the script 
# with "verbose" and one without "verbose"

# Argparse arguments:
# Files - Baselight/Flames Text files
# Xytech – Xytech file input
# Verbose – Console output on/off
# Output – to CSV or Database

# Read a script thtat imports a file and prints out the total # of lines

import sys
import argparse 

# container for argument specifications and options that apply to ther entire parser
parser = argparse.ArgumentParser(description= "Return number of lines in a text file")

parser.add_argument("--files", dest= "workFiles", help = "files to process")
parser.add_argument("--verbose", action= "store_true",  help = "show verbose")
args = parser.parse_args()

# print(args.workFiles)
files = open(args.workFiles,'r').readlines()
if args.workFiles is None: 
    print("No files selected")
    sys.exit(2)
else:
    job = args.workFiles

if args.verbose: 
    print("This is verbose!")
    for line in files:
        print(line)
print(len(files))
    