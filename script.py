import re
import sys

if(len(sys.argv) == 1):
    print("usage : python3 script.py morse_pattern [first_letter]")
    exit(1)

morse = sys.argv[1]

if(re.match('^[\.-]*$', morse) == None):
    print("usage : python3 script.py morse_pattern [first_letter]")
    exit(1)

startWith = sys.argv[2].lower() if len(sys.argv) == 3 else None

pattern = '^[^aeiuyéèoô]*' + '[^aeiuyéèoô]*'.join(morse) + '[^aeiuyéèoô]*$'
pattern = pattern.replace('.', '[aeiuyéè]').replace('-', '[oô]')

file = open("dico.txt", "r")
words = [line.rstrip('\n').lower() for line in file]

for word in words:
    if(re.match(pattern, word) != None):
        if(startWith == None):
            print(word)
            continue
        
        if(word.startswith(startWith, )):
            print(word)
