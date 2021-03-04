a = {}
a[1] = 1
a['1'] = 2
a[1.0]=4

count = 0

print(a)

for i in a:
    count += a[i]
print(count)