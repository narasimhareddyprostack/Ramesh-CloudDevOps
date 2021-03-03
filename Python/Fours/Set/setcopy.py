'''
Shallow copy is a bit-wise copy of an object. 
A new object is created that has an exact copy of the values in the original object
'''
s = {1,2,3}
new_set = s
print(s)
print(new_set)


'''
The copy() method returns a shallow copy of the set.
The copy() method in Python returns a copy of the Set. 
We can copy a set to another set using the = operator, 

however copying a set using = operator means that 
    -when we change the new set the copied set will also be changed,
'''
s.remove(3)
print(s)
print(new_set)

'''
copy means - reference
'''