#Useful Operators
#Operators- operators are special symbols that designate that some sort of computation should be performed.

myList = [1,2,3]
#range
for num in range(3,10,2):#range(starts,ends,stepsize)
    print(num)

print(list(range(0,11,2)))

#index operator
index_count = 0
word = 'abcde'
for letter in word:
    print('At index {} the letter is {}'.format(index_count,letter))
    index_count = index_count+1

#enumerate function
for item in enumerate(word):
    print(item) 

#zip function
myList = [1,2,3]
myLetters = ['a','b','c']

for item in zip (myList,myLetters):
    print(item)

print(list(zip(myList,myLetters)))

#in operator checks if list has the value needed
print('x' in myLetters) #returns boolean value-False

#can be used in dictionaries
print('myKey'in{'myKey':345})
d ={'myKey':345}
print(345 in d.keys())

#min 
myList = [1,2,3]
print(min(myList))
#max
print(max(myList))

##random Library
from random import shuffle
myList = [1,2,3,4,5,6,7,8,9,10]
shuffle(myList)#shuffles a list
print(myList)

from random import randint
randomInt = randint(0,100) #random int from a certain range
print(randomInt)

result = input('Enter a number here: ')#imput function **always going to return a string

int(result)#use casts to change the datatype of value





