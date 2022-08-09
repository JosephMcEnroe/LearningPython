#Functions allow us to create blocks of code that can be easily executed many times, without
#needing to constantly rewrite the code

#def - keyword that is need to create methods
#ex: def name_of_function():
#       "
#          Doctring that explains function
#       "
#       Code the method is in

from distutils.command import check
from doctest import Example


def say_hello():
    print('Hello')

say_hello()

num1 = 61
num2 = 62

def sum_of_num(num1,num2):
    return num1+num2

print(sum_of_num(num1,num2))

def even_number(number):
    return number%2 == 0
print(even_number(4)) #true 
print(even_number(5)) #false

#RETURNS TRUE IF ANY NUMBER IS EVEN 
def check_even_list(num_List):
    #returns true if even
    for number in num_List:
        if number %2 == 0:
            return True
    return False
            

jeff = check_even_list([1,2,3,4])
print(jeff)

jeff = check_even_list([1,1,3,4])
print(jeff)

jeff = check_even_list([1,3,5])
print(jeff)

def check_even_list(num_List):
    #returns alls the even nums in a list

    #placeholder varaibles
    even_numbers = []
    
    for number in num_List:
        if number %2 == 0:
            even_numbers.append(number)
        else:
            pass
    return even_numbers

jeff = check_even_list([1,3,5,4,6])
print(jeff)

##Tuple Functions
stock_prices = [('APPL',200),('GOOG',400),('MSFT',100)]
for item in stock_prices:
    print(item)
for ticker, price in stock_prices:
    print(price+(0.1*price))

work_hours = [('Abby',100),('Billy',400),('Cassie',800)]

def employee_check(work_hours):
    
    #returns employee with the highest amount of hours
    current_max = 0
    employee_of_month = ''

    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_month = employee
        else:
            pass

    #return
    return(employee_of_month,current_max)

name,hours = employee_check(work_hours)

print(name)
print(hours)

#interactions
example = [1,2,3,4,5,6,7,8]

from random import sample, shuffle

shuffle(example)

print(example)

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

result = shuffle_list(example)

print(result) 

mylist = ['','0',' ']

def player_guess():
    guess = ''

    while guess not in ['0','1','2']:
        guess = input("Pick a number: 0,1 or 2")
    
    return int(guess)



def check_guess(mylist,guess):
    if mylist[guess] == '0':
        print("Correct!")
    else: 
        print("Wrong guess!")
        print(mylist)
        
mylist = shuffle_list(mylist)
guess = player_guess()
check_guess(mylist,guess)


