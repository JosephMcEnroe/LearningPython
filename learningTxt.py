from importlib.resources import contents


myfile = open('myfile.txt')
myfile.seek(0)#resets the point of the document back to zero
print(myfile.read()) #read method reads the document 
myfile.close() 
#with('myfile.txt') as my_new_file : contents = my_new_file.read() figure out later
with open('myfile.txt', mode = 'r') as myfile: contents = myfile.read() 
#mode = 'r' == read, mode = 'w' == write, mode = 'a' == append to files,  mode = 'r+' == reading and writing 
#mode = 'w+' == writing and reading

myfile = open('my_new_file.txt', 'w')
myfile.write('Hello World')
myfile.write('It is a beautiful day')

#with open('my_new_file.txt', mode = 'w') as myfile : contents = 'HELLO WORLD' #HELLO WORLD doesn't show up in the txt file
#print(contents)#checks the contents is full

#IF TRYING TO GET FILE OUTSIDE OF PYTHON SCRIPT FILE USE
# (MAC)     myfile = open(/User/UserName/Folder/Test.txt)
# (WINDOWS) myfile = open(C:\\User\\UserName\\Folder\\Test.txt)
