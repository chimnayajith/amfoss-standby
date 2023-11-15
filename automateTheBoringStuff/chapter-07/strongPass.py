import re

def isStrong(pasw):
    if(len(pasw)<8):
        return False
    
    upperRegex = re.compile(r'[A-Z]')
    if upperRegex.search(pasw) is None:
        return False

    lowerRegex = re.compile(r'[a-z]')
    if lowerRegex.search(pasw) is None:
        return False
    
    digitRegex = re.compile(r'\d')
    if digitRegex.search(pasw) is None:
        return False
    return True



password = input()
if isStrong(password):
    print("ok")
else:
    print("not ok")
