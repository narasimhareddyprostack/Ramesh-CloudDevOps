'''
copy()  ==> copy the key-value pairs into another obj
a = d.copy()
'''
d = {'name':'Naraimha', 'age':37}
a = d.copy()
d['name'] = 'Naraimha Reddy'
print(a)
print(d)


'''
items() # display alll key -value pairs
'''
print(d.items())

'''
keys()  # display all keys
values() # display all values of dict
'''
