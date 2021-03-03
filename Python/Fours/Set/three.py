s = {10,20,30}
# set is mutable ang growable object
s.update((10,20,30))
print(s)
# s.add(40,50)  # add() takes exactly one argument - TypeError

'''
add vs update
1)add() accepts a single parameter, whereas update() can accept multiple sequences.
2)add() is faster than update().
3)Use add() function to add a single element. 
    Whereas use update() function to add multiple elements to the set.
4)add() accepts a single parameter, whereas update() can accept multiple sequences.

Example:
sample_set = {"Hi", "This", "is", 4, 3, 3}
sample_set.update([11, 12], (21, 22), [31, 32])
print(sample_set)
{32, 'is', 3, 'This', 4, 'Hi', 11, 12, 21, 22, 31}

'''
print(max(s))
print(sum(s))


# Set - indexing and slicing not applicable
# Set - Duplicates not allowed
# Order in guarantee
