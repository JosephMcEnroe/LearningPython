#Learning about control flow if statements

#keywords- if,elif,else
#using indentation system that is very different from other programming languages and is very important to python

#if some_condition:
    #excute some code
#elif some_other_condidtion
    #do something different
#else:
    #do something else
hungry = False

if hungry:
    print('FEED ME')#print if true
else: 
    print('not hungry')#print if false

loc = 'Bank'

if loc == 'Auto Shop':
    print('Cars are cool!')
else:
    print("I don't know much")