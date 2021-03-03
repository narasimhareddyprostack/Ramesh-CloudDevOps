#1) accessing dict values using keys in python
# Dict - name followed by squre bracket & in the [] 
# we specity the key for which we want the value 

d = { 'name':'Narasimha'}
print(d['name'])

'''
print(d[name])
NameError: name 'name' is not defined
'''

#2) changing the value in Dict
# To update the value in dict we are using corresponding key.

'''
3)  Adding a new entry 
4)Loop/Iterate 
for e in mydict:
    print("Key:", e, "Value:" , mydict[e])
'''

'''
5) Delete Operation dict
1) we can delete key-value pairs and as well as entire dictionary
'''
print(d)
del d['name']  # remove the entire key
print(d)
'''
{'name': 'Narasimha'}
{}
'''
'''
d.clear()  # remove all key-value pair from the dict.
del d   # delete entire dict obj
'''