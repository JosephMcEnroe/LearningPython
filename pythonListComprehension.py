#List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
from unittest import result


mystring = 'hello'

mylist = []

for letter in mystring:
    mylist.append(letter)

mylist= [letter for letter in mystring] # this is does the same function as the for loop above
print(mylist)

mylist = [x for x in 'word'] #as long as "x" is the same character or phrase as the loop control it works
print(mylist)

mylist= [num**2  for num in range(0,11)] #the first object in the brackets is called the expression(it both the input and output) it controls what is outputed
print(mylist)

mylist= [num  for num in range(0,11) if num%2==0]# can also add if statements in there
print(mylist)

celcius = [0,10,20,34.5]
fahrenheit = [((9/5)*temp+32) for temp in celcius]
print(fahrenheit)

results = [x if x%2==0 else 'ODD' for x in range(0,11)] #dont do this lol, readablity and reproducible
print(results)


