import re

f = open("ingest_this.txt", "r")
words = f.readlines()
vowels = "[aeiouAEIOU]"

for character in words:
    print(re.sub(vowels, "9", character))
