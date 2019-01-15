'''
Objective:
Using a dictionary dict translate a text into a new_text
Need to be familiar with:
Data Structure :https://docs.python.org/3/tutorial/datastructures.html
                5.1 lists
                5.5  dictionary
'''

dict = {'Name': 'Nameless One', 'Strength': 'Very powerful skills' , 'Class' : 'warrior'}

# print("dict['Name']", dict['Name'])
# print(dict.keys())
# print(dict.values())

# Translate a text using a dictionary

text = "This is a simple text to check whether the Name as a character" \
       " having good Strength could be replacing a Class fighter"
print (text)
text_list = text.split(' ')
# print( text_list)
for i in range(len( text_list)):
    for key in dict.keys():
        if text_list[i] == key:
            text_list.remove(text_list[i])
            text_list.insert( i, dict[key] )


new_text = ''
for word in text_list:
    new_text = new_text +  ' ' + word
print(new_text)
