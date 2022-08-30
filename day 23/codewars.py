#N1 
def lovefunc( flower1, flower2 ):
    if (flower1%2==0 and flower2%2==1) or (flower1%2==1 and flower2%2==0):
        return True
    else:
        return False

def lovefunc( flower1, flower2 ):
    return (flower1+flower2)%2

#N2 homework of wed 
arr = "nika zuka gabrieli gio saba andria daviti"

# output = ["nika1", "zuka2", "gabrieli3"]

#step1 create an array from string
splitted_arr = arr.split()

final_arr = []

for i in range(0, len(splitted_arr)):
    final_arr.append(splitted_arr[i]+str(i+1))

print(final_arr)

#N3 
def multiply(number1, number2):
    return "{} * {} = {}".format(number1, number2, number1 * number2)

print(multiply(10, 5))

#N4
def rental_car_cost(d):
    result = d * 40 

    if d < 3:
        return result - 0 
    elif d >= 3 and d<7:
        return result - 20 
    elif d>=7:
        return result - 50
    
    
#N5
def string_to_array(s):
    if s == "":
        return [""]

    splited_arr = s.split()
    return splited_arr

#N6
def bonus_time(salary, bonus):
    if bonus == True:
        return "${}".format(salary * 10)
    elif bonus == False:
        return "${}".format(salary)