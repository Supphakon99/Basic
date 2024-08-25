"""
#
#part: python Function
#
"""
def myFunction():
    i = 1
    while i <= 3:
        print("Hell World ", i)
        i+=1
myFunction()
myFunction()

# parameter
def myName(name):
    print("My name is " + name)
myName("Anya")
myName("Loid")

def myFullName(first_name = "unknown", last_name = "Forger"):
    print("My name is " + first_name  + " " + last_name)
myFullName("Anya")
myFullName("Anya", "Forger")
myFullName("Yor", "Forger")
myFullName(last_name = "Forger", first_name="Loid")

def myFruits(frits):
    for fruit in frits:
        print(frits)
fruits = ["Apple", "Banana", "Coconut"]
myFruits(fruits)
def red_potion(hp):
    return hp + 50

print("HP: ", red_potion(100))
print("HP: ", red_potion(30))