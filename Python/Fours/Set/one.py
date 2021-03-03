x = set()
print(type(x))


x = {10,20,30,10}
print(x)

#print(x[0])  # Type Error  - 'Set' Object does not Support indexing

#print(x[1:2]) # Type Error - 'set' object is not subscriptable

x.add(50)   # set is mutable and growable

print(x)
x.remove(50)
print(x)

#x.append(50)
