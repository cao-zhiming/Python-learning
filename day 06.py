# THIS LESSON IS ABOUT THEORIES.

# id()
# value ---> address of tempStorage ---> str, int...
'''
val = 100
id(val)
'''

# is checks if the two things' tempStorage's address' the same.
# NOTE THAT SOMETIMES THE 'IS' ISN'T LIKE WHAT WE THINK: FOR EXAMPLE:
'''
value1 = ['c',2,'k']
value2 = ['c',2,'k']
print(value1 is value2)  # False
'''

# if same id, the same thing.
# if the same thing, maybe not the same id.

# code-block:
# every file is a code-block, and every line in the interactive mode is a code-block.
# same code-block: all int, bool, all str.
# not same code-block: -5~256, bool, almost all str.
'''
Python gives all the numbers from -5 to 256, 
and almost all str into a database 
before we start the program.
'''






# SET:
# /DELETE THE SAME THINGS IN A LIST.
# /THE SET ISN'T ALWAYS IN A SINGLE 1, 2, 3, UNLIKE OTHERS.
# example:
'''
set1 = {1, 'test',False,'...'}
print(set1)
'''

# same things in more sets:
# /intersection
'''
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
print(set1 & set2) # {4,5}
'''
# /union
'''
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
print(set1 | set2) # {1,2,3,4,5,6,7,8}
'''
# /difference
'''
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
print(set1 - set2) # {1,2,3}
'''
# /symmetric_difference
'''
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
print(set1 ^ set2) # {1,2,3,6,7,8}
'''

# /delete the same things in a list
'''
my_list = [1,'this is a str', False,False,1,2,3,7,1,1,1,'this is a str']
set1 = set(my_list)
my_list = list(set1)
print(my_list)
# [False, 1, 2, 3, 7, 'this is a str']
'''


# DARK LIGHT COPY:

# light copy
lista = [1,2,3,4,5]
listb = lista.copy()
# CAUTION:
'''
NOW, IF WE CHANGE SOMETHING IN LISTA,
LISTA WILL CHANGE(IF OUR CODE IS RIGHT), 
BUT LISTB WON'T.
'''

# deep copy
import copy
listc = copy.deepcopy(lista)
print(listc)


