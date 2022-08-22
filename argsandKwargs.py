def myfunc(a,b,c=0,d=0): #problem with this is that it is a set about of values meanig the program will error
                        #out
    #Returns 5% of the sum of a and b 
    return sum((a,b,c,d)) * 0.05

print(myfunc(40,60,300))

def myfunc(*args):
    return sum(args) * 0.05 #args can be any word

myfunc(5,3,500)# args can pass in as many arguments as you want 

def myfunc(*args):
    for item in args:
        print(item)

myfunc(5,3,500)
 
def myfunc(**kwargs): #double ** returns dictionary
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')
myfunc(fruit = 'apple', veggie = 'lettuce') # my choice of fruit is apple


def myfunc(*args,**kwargs):
    print('I would like {} {}'.format(args[0], kwargs['food']))

myfunc(10,20,30,fruit = 'orange',food = 'eggs', animal = 'dog')


def myfunc(*args):
    
    count = 0
    newWord = ''
    for word in args:
        if count % 2 != 0:
            newWord.append(word.upper())
        else:
            newWord.append(word)
            
    count+=1
    return args


