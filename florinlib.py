'''
Python math library :
https://docs.python.org/3/library/math.html

'''

# function to determine the distance between two points (2D)
import math
#
#
# def distance2d(x1,y1,x2,y2):
#
#     dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
#     return dist
#
#
# print(distance2d(0,0, 3,4))
#
#
# def distance3d(x1,y1,z1,x2,y2,z2):
#
#     dist = math.sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)
#     return dist
#
# print(distance3d(0,0,0,3,4,12))

word = list("whateveryouwant")
print(word)

# create a function to eliminate the repeating letters
# and keep only the first one of them, inn order of its apparition

def elimi_repeat(alist):
    # create a new list that contains only one of the repeating letters,
    # in order of its apparotion

    new = []
    for let in alist:
        if let not in new:
            new.append(let)

    return new


print(elimi_repeat(word))

# create a function to diplay the indexes where a certain letter is a alist
# if a letter appears multiple times, than the letter is followed by the list of indexes


def element_and_index(alist):
    tuplist =[]
    for ind , value in enumerate(alist):
        print(ind, value)
        tuplist.append((value, ind))
    new = elimi_repeat(alist)
    for let in new:
        u =[let]
        for pair in tuplist:
            if let == pair[0]:
                u.append(pair[1])
        print(u)


    return tuplist



#
element_and_index(word)

print(element_and_index(word))