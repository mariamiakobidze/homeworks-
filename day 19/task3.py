#Beginner Series 1 School Paperwork
def paperwork(n, m):
    if n < 0 or m <0:
        return 0 
    else:
        return n * m 
#Opposites Attract
def lovefunc( flower1, flower2 ):
    if flower1 == flower2:
        return False 
    else:
        return True
def lovefunc( flower1, flower2 ):
    return (flower1+flower2)%2
#
def reverse_seq(n):
    arr = []
    while n > 0:
        arr.append(n)
        n -= 1 

    return arr

