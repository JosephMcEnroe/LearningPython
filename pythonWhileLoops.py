#Learning about While Liips
# while some_boolean_conditon:
#else: #do something different
#
#break : breaks out of the current closst enclosing loop 
#continue: goes to the top of the closest enclosing loop
#pass: Does Nothing at all

x = 0
while  x<=5:
    print(x)
    x +=1 
else:
    print('X is not less than 5')

myString = 'Joseph'
for letter in myString:
    if letter == 'o':
        continue #sents the loop back to the beginning avoiding 'o'
    print(letter)

for letter in myString:
    if letter == 's':
        break #ends the loop
    print(letter)