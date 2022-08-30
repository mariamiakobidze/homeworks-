#N1 
def summation(num):
    temp_sum = 0 
    
    for i in range (1, num+1):
        temp_sum += i
        
    return temp_sum
#N2
def count_sheeps(sheep):  
    return sheep.count(True)
#N3
def My_Function(greet):
    return("hello world")
#N4
# ამოცანა N1:


# #მომხმარებელს ფუნქციაში შეყავს 3 რიცხვი, ფუნქციამ უნდა დააბრუნოს ტექსტი: x მეტია y-ზე ,  რაღაცაჯერ,  x მეტია y-ზე რაღაცაჯერ

# #მაგალითად: 
# # პირველი რიცხვი - 10 
# # მეორე რიცხვი - 45 
# # მესამე რიცხვი 5

# #output: 45 მეტია 10-ზე 4.5ჯერ
# .                 45 მეტია 5ზე 9 ჯერ
# .
# .

# 
x = int(input("enter X:"))
y = int(input("enter Y: "))
z = int(input("enter Z:"))

def comparision_of_nums (x,y,z): 
     if x>y>z:
         return "x მეტია y-ზე" + str(x/y) + "ჯერ" + "ხოლო x მეტია z -ზე" + str(x/z) +"ჯერ"
     elif y>x>z:
         return  "y მეტია x -ზე" + str(y/x) +"ჯერ" + "ხოლო y მეტია z -ზე" + str(y/z) +"ჯერ"
     elif z>x> y:
         return "z მეტია x -ზე" + str(z/x) +"ჯერ" + "ხოლო z მეტია y -ზე" + str(z/y) +"ჯერ"

print(comparision_of_nums(x, y, z))

#N2

def shedareba (x,y,n):
    if x>y>n: 
        return()

def more(num1, num2, num3):
    num_list = [num1, num2, num3]
    num_list.sort(reverse = True)
    return "{n1} is more than {n2} {a} times and {n1} is more than {n3} {b} times".format(n1 = num_list[0], n2 = num_list[1], n3 = num_list[2], a = num_list[0]/num_list[1], b = num_list[0]/num_list[2])

more(1,2,5)
#N5


#ფუნქციაში გადაეცით არგუმენტად რამე list რომელშიც იქნება 15 random სახელი

#დამიპრინტეთ მხოლოდ ის სახელები რომლებიც იწყება a-ზე


my_list=["nika", "lasha", "giorgi", "aguri", "luka", "andria", "ani", "gvanca", "elene", "maro", "anamaria", "tamazi", "axmedi", "alina", "vashlatama"]

for element in my_list:
    if element[0] == "a":
        print("სახელი " + element + " იწყება ა-ზე")