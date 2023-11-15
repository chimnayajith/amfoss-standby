import re

datePattern = re.compile(r'(0[1-9]|[12][0-9]|[3][01])/(0[1-9]|1[0-2])/([12][0-9]{3})$')
dates = []

for each in dates:
    matches = datePattern.match(each)
    day , month , year = map(int , matches.groups())

    #conditions for being valid
    validDate = (
        (month in [1,3,5,7,8,10,12] and day<=31 ) or
        (month in [4,6,9,11] and day <=30 ) or
        (month ==2 and ((year%4==0 and year%100!=0) or (year%400==0)) and day<=29) or
        (month ==2 and day<=28)
    )

    if validDate:
        print("Valid Date")
    else:
        print("Invalid Date.")
