'''
Create a new dictionary by extracting the following keys 
from a below dictionary
keys = ["name", "salary"]
'''
sampleDict = { 
  "name": "Kelly",
  "age":25, 
  "salary": 8000, 
  "city": "New york" }

keys = ["name", "salary"]
newDict = {k:sampleDict[k] for k in keys}
print(newDict)