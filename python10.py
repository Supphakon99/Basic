"""
#
# Part: python json
# API = Application Programming Interface
#
"""
import json

# Make a json (String)
x = '{"name": "jason", "age": 20, "city": "Phuket"}'
print(x)

# parse 
y = json.loads(x)

# Python Dictionry
print(y)
print(y["city"])

a = {
    "name" : "Noa",
    "age" : 20,
    "city" : "Phuket",
}

# convert into JSON(String)
b = json.dumps(a)

# JSON String
print(b)


