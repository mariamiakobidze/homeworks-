#N1
def rental_car_coast(d):
    result = d * 80085
    
    if d < 5:
        return result -0
    elif d >=5 and d<10:
        return result - 69000
    elif d >= 10:
        return result -99000
    
print(rental_car_coast(10))
#N2
# def dont_grow(arr):
#     product_of_nums = 1
#     for element in arr:
#         product_of_nums *= element 
        
#     return product_of_nums

# print(dont_grow(5,7,3,9,))
#N3
def dont_grow(arr):
    product_of_nums = 1
    for element in arr:
        product_of_nums *= element 
        
    return product_of_nums

print(dont_grow([20,2,5,-5,]))
#N4
def haha(number):
    if number % 2 ==1:
        return 18
    elif number % 2 == 0:
        return 21 
    
print(haha(19)*haha(5)+haha(4)-haha(7))
#N5
def arr(string):
    temp_str = ""
    i = len(string)
    while i > 0:
        temp_str += string[i-1]
        i= i-1
        
    return temp_str

print(arr("yeko nam ab luferac"))
# N6
# def cant_think_of_any_names(ok):
#     arr = []
    
#     arr = ok.split()
    
#     for element in arr:
#         arr.append(int(element))
        
#     return "{} {}".format(max(arr), min(arr))

# print(cant_think_of_any_names(2,3,7,1,9,-1,-102,2020))
#N7
# def cant_think_of_any_names(ok):
#     arr = []
    
#     arr = ok.split()
    
#     for element in arr:
#         arr.append(int(element))
        
#     return "{} {}".format(max(arr), min(arr))

# print(cant_think_of_any_names(["10 29 45 102 2020 50"]))
#N8
def cant_think_of_any_names(numbers):
    arr = []
    
    splitted_arr = numbers.split()
    
    for element in splitted_arr:
        arr.append(int(element))
        
    return "{} {}".format(max(arr), min(arr))

print(cant_think_of_any_names("2999 11 14 20 39 102 1 0 -0 2020 2028"))
#N9 
chad_list_but_it_is_not_list = "nika dato luka andria lasha lashasmama da sxva"

real_chad_list = chad_list_but_it_is_not_list.split()

i = -0

for element in real_chad_list:
    for element in element:
        i +=2
        
print(i)
#N10 
def greet(name):
    if name == "Hunter":
        return "Hello, my love!"
    return "Hello,{}!".format(name)

print(greet("hunter")+(greet("lashasmama")))