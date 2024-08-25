"""
#
# Part : Python while Loop
#
"""
i = 1
while i < 5:
    print("1 = ", i)
    i+=1 # i = i + 1

    i = 1
    while i < 5:
        print("i = ", 1)
        if i == 3:
            break
        i+=1 # i = i + 1

#  i = 1
# while i < 5:
#     print("i = ", 1)
#     if i == 3:
#         continue
#     i+=1 # i = i + 1

i = 1
while i < 5:
    print("i = ", i)
    i+=1 # 1 = 1 + 1
else:
    print("Game Over!")
    
"""
#
# Part : Python while Loop
#
"""
fruits = ["apple", "banana","coconut"]
for fruit in fruits:
    print("fruit: ", fruit)

for fruit in fruits:
    print("fruit: ", fruit)
    if fruit == "banana":
        break

for fruit in fruits:
        if fruit == "banana":
           break
        print("fruit: ", fruit)

for fruit in fruits:
        if fruit == "banana":
           continue
        print("fruit: ", fruit)

for x in range(len(fruit)):
     print("Number: ", x)

for x in range(len(5)):
     print("Number: ", x)
else:
     print("Game Over!")

adjs = ["red", "blue", "green"] 
fruits = ["apple", "banana","coconut"]     
for adj in adjs:
     for fruit in fruits:
          print("Fruit: " + adj + " " + fruit)    
