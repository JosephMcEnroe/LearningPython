#Learning about list
my_list = ['strings', 100,23.2]
print(my_list) #strings 100 23.2
print(len(my_list)) #3

my_list = ["one","two","three"]
 #indexing list
print(my_list[0])#one
#slicing list
print(my_list[0:2])#1,2

#immutation
another_list = ['four,five']
my_list = my_list + another_list
print(my_list) # one two three four five

#adding new element to list
my_list.append('six') #append = adds item to end of the list
print(my_list)#one two three four five six

#deleting end of the list
popped_item = my_list.pop()
print(my_list)#one two three four five 
print(popped_item)
my_list.pop(0)#can also pop variables from beginning of the list


new_list = ['a','e','x','b','c']
num_list = [4,1,8,3]

#sorting list
new_list.sort()
print(new_list) #a b c e x

#reverse list
num_list.reverse()
print(num_list)#3814




