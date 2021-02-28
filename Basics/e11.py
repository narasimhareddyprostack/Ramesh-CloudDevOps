""" def emp_Details(name, age):
    x = "My Name is" + name
    y = "My age is " + str(age)
    z = "GM"
    return x, y, z


a = emp_Details("Nras", 38)
print(a[0]) """


def emp(a, *b):
    return a, b


a = emp('abc', 24, 'loc')
print(a)
print(a[1][0])
