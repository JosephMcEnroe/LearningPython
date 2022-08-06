#Functions allow us to create blocks of code that can be easily executed many times, without
#needing to constantly rewrite the code

#def - keyword that is need to create methods
#ex: def name_of_function():
#       "
#          Doctring that explains function
#       "
#       Code the method is in

from distutils.command import check


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