# li = [100, "h", [1,2,3]]
# print(type([-1]))

# adding things into a list:
exampleAddingList = ['apple', 'pear', 'banana']
# list.append("str of adding")
'''
exampleAddingList.append('pineapple')
print(exampleAddingList)
'''

# list.insert("place,"str of adding")
'''
exampleAddingList.insert(3, 'orange')
print(exampleAddingList)
'''

# list.extend([1, 2, 3, 'adding str'])
'''
exampleAddingList.extend(['grapes', 'peaches', 'melons'])
print(exampleAddingList)
'''


# deleting things from a list:
exampleDeletingList = ['red', 'green', 'yellow', 'blue', 'purple']
# list.pop(place)
'''
exampleDeletingList.pop(-3)
print(exampleDeletingList)
'''

# list.remove('str of deleting')
# CAUTION: IF TWO "A"S IN IT, REMOVE CAN ONLY DELETE THE FIRST ONE
'''
exampleDeletingList.remove('purple')
print(exampleDeletingList)
'''

# del:
# del list[place]
'''
del exampleDeletingList[-2]
'''
# del list[cutting]
# example: del list[:2]
'''
del exampleDeletingList [:2]
print(exampleDeletingList)
'''


# changing things to a list:
exampleChangingList = ['interesting', 'funny', 'exhausted']
# list[place] = "the str you want to change"
'''
exampleChangingList[2] = "great"
print(exampleChangingList)
'''


# SOME EXERCISES:
list_test = [1, 2, 'jdhdoiwoiewjds', [1, 'alex', 3]]
'''
/QUESTION 1 CHANGE THE 3RD SUBJECT OF THE LIST INTO CAPITAL LETTERS AND PUT THE CHANGED WORD BACK TO 
THE RIGHT PLACE OF THE LIST
/QUESTION 2 PUT 'ABCD' INTO THE SMALLER LIST
/QUETION 3 CHANGE 'alex' IN THE SMALLER LIST INTO 'ALEXANDRIA' AND PLACE IT BACK TO THE LIST
'''

# ANWSER OF Q1:
'''
list_test[2] = list_test[2].upper()
print(list_test)
'''

# ANSWER OF Q2:
'''
list_test[-1].append('ABCD')
print(list_test)
'''

# ANSWER OF Q3:
'''
list_test[-1][1] = 'ALEXANDRIA'
print(list_test)
'''