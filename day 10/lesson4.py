# N1 Multiplay
def multiply(a, b):
    a * b
# N2 Even or odd 
def even_or_odd(number):
      if number % 2 == 1:
        return "Odd"
      elif number % 2 == 0:
        return "Even"
# N3 Opposite number 
def opposite(number):
    return number *  -1  
# N4 Convert a number to a string 
def number_to_string(num):
    return str(num)
# N5 Convert boolean values to string 'Yes' or 'No'
def bool_to_word(boolean):
    if boolean == True:
        return "Yes"
    elif boolean == False:
        return "No"
# N6 Reversed stings 
def solution(string):
    return string[::-1]
# N7 Return negative 
def make_negative( number ):
    if number > 0:
        return -1 * number
    else:
        return number
# N8 Sum of positive 
def positive_sum(arr):
    return sum(i for i in arr if i > 0)

def positive_sum(arr):
    sum = 0 
    for num in arr:
        if num >= 0 :
            sum += num
    return sum       
    
def positive_sum(arr):
    temp_sum = 0   #temporary sum ( დროებითი ჯამი )

    for element in arr:
        if element > 0:
            temp_sum += element 

    return temp_sum

# N9 String repeat 
def repeat_str(repeat, string):
    return repeat * string 

def repeat_str(repeat, string):
    temp_str = ""
    for i in range (repeat):
        temp_str += string
        
    return temp_str
# N10 Remove First and Last Character
def remove_char(s):
    return s[1 : -1]
# N11 Find the smallest integer in the array
def find_smallest_int(arr):
    return min(arr)
# N12 Remove String Spaces
def no_space(x):
    temp_str = ""
    
    for char in x:
        if char != " ":
            temp_str += char
            
    return temp_str

