full_name = input("enter your name: ")

i = 0
while i < len (full_name):
    if full_name[i] in "aeiou":
        print(str(i)+ full_name[i])
        
    i += 1

age_of_user = int (input("enter users age: "))

total_price = 0 
for i in range(5):
    age_of_user= int(input("enter users age:"))
    if age_of_user >=3:
        total_price += 100
        
print(total_price)

total_price = 0 
i=0 
while i<5:
    age_of_user = int(input("enter users age:"))
    if age_of_user >= 3:
        total_price += 100
    i+= 1
print(total_price)

i = 0 
x= 0 
while i < 4:
    x** i 
    i *= 1
    
print(x)