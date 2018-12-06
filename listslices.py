'''
lists
keywords : slice, delete, clone a list

Exs:
1. Write a Python program to sum all the items in a list
2. Write a Python program to multiply all the items in a list
3. Write a Python program to count the number of strings where the string length is 2 or more
and the first and last character are same from a given list of strings.
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2
4. Write a Python program to remove duplicates from a list.
5. Write a Python program to check a list is empty or not.
6. Write a Python program to find the list of words that are longer than n from a given list of words.
7. Write a Python function that takes two lists and returns True if they have at least one common member.
8.Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. Go to the editor
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Green', 'White', 'Black']

9. Write a Python program to print the numbers of a specified list after removing even numbers from it.
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

