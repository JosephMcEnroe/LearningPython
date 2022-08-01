#Learning ForLoops 
#my_iterable = [1,2,3]
#for item_name in my_iterable:      item name == count or loop control  my_iterable is the length of the loop
#print(item_name)
#>>1
#>>2
#>>3

from multiprocessing.sharedctypes import Value


mylist = [1,2,3,4,5,6,7,8,9,10]
for num in mylist:
    print(num)

for num in mylist:
    #Check for even
    if num % 2 == 0:
         print(f'Even Number: {num}')
    else:
        print(f'Odd Number: {num}')

list_sum = 0#add all the value of the list

for num in mylist:
    list_sum = list_sum + num

print(list_sum)

myString = 'Hello World'
for letter in myString:
    print(letter)

print('\n')
tup = (1,2,3)
for _ in tup:
    print(_)

mylist = [(1,2),(3,4),(5,6),(7,8)]

for (a,b) in mylist: #Tuple unpacking creating an temporary variable to upack to the tuple
    print(a) #prints out a
    print(b) #prints out b

mylist = {'k1':1,'k2':2, 'k3':3}
for key,value in mylist.items(): #printing out dictionaries
    print(value)

for value in mylist.values(): #printing out value
    print(value)
for key in mylist.keys():
    print(key)
