#check whether item is in the set 

s = {10,20,30}
print ( 10 in s)

# iterate/loop the elements in set 
for a in s:
    print(a)

#add and remove
s.add(40)
s.remove(10)
print(s)

#s.remove(10)
#keyError 
'''
remove vs discard
The remove() method raises an error when the specified element doesn't exist
in the given set, however the discard() method doesn't raise any error 
if the specified element is not present in the set and the set remains unchanged.
'''

print(s)
