#Jenny's secret message
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {}!".format(name)
    
#Beginner Series 2 Clock
def past(h, m, s):
    return 3600000 * h + 60000 * m + 1000 * s
#Sum Arrays
def sum_array(a):
    return sum(a)
#Opposites Attract
def lovefunc( flower1, flower2 ):
    return (flower1+flower2)%2
#Find Maximum and Minimum Values of a List
def minimum(arr):
    return min(arr)

def maximum(arr):
    return max(arr)