import pyinputplus as pyip
import random, time

def quiz():
    for qs in range(10):
        num1 = random.randint(0,9)
        num2 = random.randint(0,9)

        try:
            ans = pyip.inputInt(
                prompt = f"Qs {qs+1} : {num1} x {num2} = ",
                allowRegexes =['^%s$' % (num1 * num2)],
                blockRegexes=[('.*', 'Incorrect!')],
                timeout=8, 
                limit=3
            )
            
            print("Correct")
            time.sleep(1)
        except pyip.TimeoutException:
            print("Times up!. Next Question.")
            time.sleep(1)

quiz()