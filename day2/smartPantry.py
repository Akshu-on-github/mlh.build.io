def checkPantry(choice):
    print("Let's check the ingredients at hand")
    
    required = {}
    pantry = {}
    
    pantry["eggs"] = float(input("Enter number of eggs: "))
    pantry["oil"] = float(input("Enter spoons of oil: "))
    pantry["milk"] = float(input("Enter cups of milk: "))
    pantry["bread_slices"] = float(input("Enter number of slices of bread: "))
    pantry["salt"] = float(input("Enter spoons of salt: "))
    pantry["sugar"] = float(input("Enter spoons of sugar: "))
    
    if recipies[choice]["eggs"] > pantry["eggs"]:
        required["eggs"] = recipies[choice]["eggs"] - pantry["eggs"]
    if recipies[choice]["oil"] > pantry["oil"]:
        required["oil"] = recipies[choice]["oil"] - pantry["oil"]
    if recipies[choice]["milk"] > pantry["milk"]:
        required["milk"] = recipies[choice]["milk"] - pantry["milk"]
    if recipies[choice]["bread_slices"] > pantry["bread_slices"]:
        required["bread_slices"] = recipies[choice]["bread_slices"] - pantry["bread_slices"]
    if recipies[choice]["salt"] > pantry["salt"]:
        required["salt"] = recipies[choice]["salt"] - pantry["salt"]
    if recipies[choice]["sugar"] > pantry["sugar"]:
        required["sugar"] = recipies[choice]["sugar"] - pantry["sugar"]
    
    if not required:
        print("You're all set!")
    else:
        print("You'll need...")
        for k, v in required:
            print(v, "units of", k)

def addRecipie(name):
    print("Let's take a look at what you're recipie will need...")
    Recipie = {}
    Recipie["eggs"] = float(input("Enter number of eggs: "))
    Recipie["oil"] = float(input("Enter spoons of oil: "))
    Recipie["milk"] = float(input("Enter cups of milk: "))
    Recipie["bread_slices"] = float(input("Enter number of slices of bread: "))
    Recipie["salt"] = float(input("Enter spoons of salt: "))
    Recipie["sugar"] = float(input("Enter spoons of sugar: "))
    recipies[name] = Recipie
    checkPantry(name)


recipies = {
    "scrambled_eggs" : {"eggs": 1, "oil": 1, "milk": 0, "bread_slices": 0, "salt": 0.5, "sugar": 0},
    "french_toast" : {"eggs": 2, "oil": 1, "milk": 0.5, "bread_slices": 10, "salt": 0, "sugar": 0.5},
    "warm_milk" : {"eggs": 0, "oil": 0, "milk": 1, "bread_slices": 0, "salt": 0, "sugar": 2},
}

def start():
    choice = input("What do you want to make today? ")
    if choice != "scrambled_eggs" and choice != "french_toast" and choice != "warm_milk":
        ch = input("\nHmm, I don't know that recipie...\nWould you like to add a new recipie to the list(Y/N)? ")
        if ch == 'Y':
            addRecipie(choice)
        else:
            ch = input("Do you want to try another recipie(Y/N)? ")
            if ch == 'Y':
                start()
    else:
        checkPantry(choice)
    

start()
print("Thank you!")
