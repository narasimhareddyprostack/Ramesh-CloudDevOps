""" from sys import argv
print(int(argv[1])+int(argv[2]))


# + operator always consider as contatination
# is predefined module
# argv - is variable, present inside sys module
# cla - default it consider as string we need to typecast

 """
from sys import argv
x = argv[1:]
print(x)
sum = 0
for x in x:
    sum = sum + int(x)
print(sum)