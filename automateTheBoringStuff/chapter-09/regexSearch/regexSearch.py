import os , re
from pathlib import Path

pattern = input("Enter the expression regex to find : ")
regex = re.compile(pattern)

examplesFolder =Path(__file__).parent / "examples"

for file in os.listdir(examplesFolder):
    with open(examplesFolder/file , 'r') as each:
        print(f"Matches for {file}")
        for num , line in enumerate(each):
            matches = regex.findall(line)
            if matches:
                print(f"Line {num+1} : {line}")
                print(f"Matched strings : {matches}")