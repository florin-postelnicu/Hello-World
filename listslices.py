'''
lists
keywords : slice, delete, clone a list

'''

mylist = ["a", "b", "c", "d", "e"]
print(mylist)
# Slice a list
print(mylist[1:3])
mylist[1:3] = ["x", "y"]
print(mylist)
print(mylist[0:])

# Squeezing elements into an empty slice at a desired location
mylist[1:1] = ["m", "n", "o", "p"]

print(mylist)
print(mylist[1])
print(mylist[4])

# Removing elements by assigning an empty slice
mylist[1:3] = []
print(mylist)

# Deleting elements of a list

del mylist[0]
print(mylist)


# cloning lists

alist = mylist[:]
print(alist)
blist = mylist
print(blist)

