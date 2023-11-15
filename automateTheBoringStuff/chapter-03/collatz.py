def collatz(num):
    if(num%2 == 0):
        return num//2
    else:
        return 3*num + 1

print("Enter number:")
n = int(input())

while True:
    n=collatz(n)
    print(n)
    if(n==1):
        break