file = open('lesson4.txt', 'r').readlines()

for f in file:
    currLine = (f.rstrip("\n"))
    if currLine.__contains__(" "):
        print(f'File: {currLine} has an error')
        print(f'The file will now be fixed:')
        print(f'{currLine.replace(" ","")}')
    else:
        print(f'File #{f} is fine and has no errors.')