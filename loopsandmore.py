
'''
Resources for use of for loop in Python :
https://www.python-course.eu/python3_for_loop.php

Resources for formatting the output of print() statement:
https://www.python-course.eu/python3_formatted_output.php
'''

for i in range(1, 10):
    print(i)
for j in range(1,10):
    print(j, end="")
print()
for k in range (1, 10):
    print(k, "",end='', flush=True)
print()

# Formatted output

#  https://www.python-course.eu/python3_formatted_output.php

for i in range( 1, 10):
    print(' {0:5d}'.format(i))


# nested loops

for row in range(1,10):
    for col in range (1,5):
        print(row, col, '  ', end='')
    print()

print(i, j,k)