#N1 
def basic_op(operator, value1, value2):
    if operator=="+":
        return value1+value2
    elif operator=="-":
        return value1-value2
    elif operator=="/":
        return value1/value2
    elif operator=="*":
        return value1*value2
    
#N2
def string_to_number(s):
    return int(s)
#N3
def century(year):

    if year%100 != 0:
        return year // 100 + 1 
    else:
        return year // 100
#N4
def litres(time):
    return int(time/2)
#N5 
def abbrev_name(name):
    
    arr_of_names = name.split()
    
    final_str = ""
    final_str += arr_of_names[0][0].upper()
    final_str += "."
    final_str += arr_of_names[1][0].upper()

    return final_str

