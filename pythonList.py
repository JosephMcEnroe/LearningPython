#Learning about list
my_list = ['strings', 100,23.2]
print(my_list) #strings 100 23.2
print(len(my_list)) #3

my_list = ["one","two","three"]
 #indexing list
print(my_list[0])#one

#slicing list
print(my_list[0:2])#one, two
print(my_list[:-1]) #one, two if the value is at the right side of the colon, 
print(my_list[-1:]) #one, two

#immutation
another_list = ['four,five']
my_list = my_list + another_list
print(my_list) # one two three four five

#adding new element to list
my_list.append('six') #append = adds item to end of the list
print(my_list)#one two three four five six

#pop method
#can delete values at any part of the list
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

#insert list
#insert method adds a value at a certain place at a list LISTNAME.insert(place you want to insert value(number), value)
new_list = ["Apples","Pineapple","Oranges"]
new_list.insert(-1,"banana")#insert banana at the end of the list
print(new_list)

#creating list using range ||  variable = range(how big you want your list)
number_list = range(9)
print(list(number_list)) #0, 1,2,3,4,5,6,7,8
print(number_list)# range(0,9)

number_list = range(2,9)
print(list(number_list))#2,3,4,5,6,7,8


#Count Method
#counts about how many times said value shows up in a list
votes = ["Jake", "Jake", "Laurie", "Laurie", "Laurie", "Jake", "Jake", "Jake", "Laurie", "Cassie", "Cassie", "Jake", "Jake", "Cassie", "Laurie", "Cassie", "Jake", "Jake", "Cassie", "Laurie"]
votes_for_jake = votes.count("Jake")
print(votes_for_jake)
