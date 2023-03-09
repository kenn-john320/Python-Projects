file = open('lesson4.txt', 'r').readlines()

for f in file:
    currLine = (f.rstrip("\n"))
    if currLine.__contains__(" "):
        print(f'File #{f} has an error')
    else:
        print(f'File #{f} is fine and has no errors.')