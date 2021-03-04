'''
Rename key city to location in the following dictionary
'''
sampleDict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
""" print(sampleDict.pop('city')) """
sampleDict['location'] = sampleDict.pop('city')
print(sampleDict)