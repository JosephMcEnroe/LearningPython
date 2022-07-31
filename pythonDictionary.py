#Learning about Dictionaries
my_dict = {'key1':'value1', 'key2':'value2'}# key1 = key of dictionary, value1 = value of the key
print(my_dict['key1'])#value1
print(my_dict['key2'])#value2

#complex dictionary
my_dict = {'key1':'123','key2':[0,1,2],'key3':{'insideKey':100}}
print(my_dict['key3']) #{'insideKey': 100}
print(my_dict['key3']['insideKey']) #100

my_dict={'key1':['a','b','c']}
print(my_dict['key1'][2].upper()) #name[key][index]

#methods
print(my_dict.keys())#returns all of the keys
print(my_dict.values())#returns of the values
print(my_dict.items())#returns of the pairings




