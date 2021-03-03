'''
update() -- add or more items into existing dict

'''
d = {'name':'Naraimha', 'age':37}
d.update({'name':'Narasimha Reddy', 'loc':'Bangalore'})
print(d)

# {'name': 'Narasimha Reddy', 'age': 37, 'loc': 'Bangalore'}

'''
pop()  # delete an item from a dict & return the removed valued
       # delte an item from a dict & return  the value of a key which was removed
'''
'''
    del d['loc']                vs                  d.pop('loc')
    remove the key& vlaue               remove the key and value and return the value

'''
x = d.pop('loc')
print(d)
print(x)

