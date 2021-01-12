import datetime

def generateRand(n, m):
    r = datetime.datetime.now().microsecond % m
    if r < n:
        if r+n < m:
            r += n
        else:
            r = m
    print(r)

def start():
    print("Enter the range you'd like to generate numbers in")
    n = int(input("Enter the minimum value: "))
    m = int(input("Enter the maximum value: "))
    if n<m:
        t = int(input("How many values do you want to generate? "))
        for i in range(t+1):
            generateRand(n, m+1)
    else:
        print("\nThe first number should be smaller than the second")
        print("Please try again\n")
        start()

start()
print("\nThanks for trying out the randomNumberGenerator!")
        
