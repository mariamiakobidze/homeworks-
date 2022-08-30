#N1 Square(n) Sum
def square_sum(numbers):
    return sum(num1 *num1  for num1 in numbers)
#N2 Convert number to reversed array of digits
def digitize(n):
    return [int(i)for i in str(n)[::-1]]
#N3 Convert a Boolean to a String
def boolean_to_string(b):
    return str(b)
#N4 Beginner - Lost Without a Map
def maps(a):
    new_arr =[]
    for element in a:
        new_arr.append = (element * 2)
        
    return new_arr
#N5 Beginner - Lost Without a Map
def maps(a):
    new_arr = []
    for element in a:
        new_arr.append(element*2)

    return new_arr
#N6 A Needle in the Haystack
def find_needle(haystack):
    index = haystack.index("needle")
    return "found the needle at position {}" .format(index)
#N7 Is n divisible by x and y?
def is_divisible(n,x,y):
    return n % x ==0 and n % y == 0
#N8MakeUpperCase
def make_upper_case(s):
    return s.upper()
