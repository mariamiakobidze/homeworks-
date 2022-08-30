#N1
def sum_array(a):
    my_sum = 0
    
    for element in a:
        my_sum += element 
    
    return my_sum

#N2
def digital_root(n):
    if n == 0:
        return 0
    if n % 9 ==0: 
        return 9
    else:
        return n% 9
    
def solution(string):
#     temp_str = ""
#     i = len(string)
#     while i > 0:
#         temp_str += string[i-1]           #chad-ური ამოხსნა
#         i = i - 1 

#     return temp_str 


#   virgin-ული ამოხსნა
    return string[::-1]
