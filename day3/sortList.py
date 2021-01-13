def alphabetical(ch):
    li = list(input("Please enter the space-seperated values to be sorted: ").split())
    li.sort()
    if ch[0] == '2' :
        li.reverse()
    print(li)

def randomize():
    import random
    print("You've found the secret order!")
    li = list(input("Please enter the space-seperated values to be sorted: ").split())
    random.shuffle(li,random.random)
    print(li)

print("Enter how you'd like to sort your contents")
print("1 - Alphabetical order")
print("2 - Reverse alphabetical order")
ch = input("Enter the number corresponding to your choice here: ")
if ch=='1' or ch=='2':
    alphabetical(ch)
else:
    randomize()
