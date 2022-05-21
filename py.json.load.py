# SAVE structure to ----> JSON file
from json  import loads
# data structure (Python)
person = {
    "name" : "John",
    "age"  : 30,
    "alive": True,
    "interests":[
        "programing",
        "hacking",
        "exe"
    ]
}

# save the data
file = open("person.json","r")
person =file.read()
file.close()

print(person)
