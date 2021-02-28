x = [10,20,30]
""" b =x.append(40)
a = x.pop()
print(a)
print(b)
print(x)
 """
a = [40,50]
x.extend(a)
print(x)
x.insert(0,10.5)
print(x)

x[0] = 10.8
print(x)

x.remove(10)
print(x)

x.pop()
print(x)

x.reverse()
print(x)
a = x.copy()
b = x
x[0] = 40.5

print(a)

print(x)
print(b)
print(a)
print(id(x), id(a), id(b))
