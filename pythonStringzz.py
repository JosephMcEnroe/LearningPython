#Learning about indexing
myString = "Hello World"

print(myString[0]) #H  
print(myString[1])  #E
print(myString[2])#L
print(myString[3])#L
print(myString[4])#0
print(myString[5])#W
print(myString[6])#O

print('\n'+myString[-1])#D
print(myString[-2])#L
print(myString[-3])#R
print(myString[-4])#O

#could also index like this
print('\n\nHelloWorld'[4]+'\n')


#Learning about splicing
myString = "abcdefghijklmnop"

print(myString[2:]) #cdefghijklmnop
print(myString[:3]) #adc *note- :3 = up to d but not included
print(myString[3:6]) #def
print(myString[1:3]) #bc

#Learning about stepsize
print(myString[::2]) #jumps two steps
print(myString[::3]) #jumps three steps
print(myString[::-1]) #prints in reverse
