import re

def madLibs(text):
    matches = re.findall(r'ADJECTIVE|NOUN|ADVERB|VERB' , text)
    for each in matches:
        rep = input(f"Enter {each.lower()}:\n")
        text = re.sub(each , rep , text , count = 1)

    return text

with open('madLibs-org.txt' , 'r') as file:
    text = file.read()

newText = madLibs(text)
print(newText)
with open('madLibs-res.txt' , 'w') as file:
    file.write(newText)