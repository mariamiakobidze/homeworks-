#მომხმარებელს შემოატანინეთ ორი რიცხვი 
# 1) ასზე დიდი 
# 2) ათსა და ოცს შორის

# თუ ვერ შეასრულებს ამ ორ პირობას იუზერი, მაშინ დაუწერეთ რომ ის დებილია
# თუ არადა, გამოიტანეთ ეკრანზე, რამდენჯერ მოთავსდება რიცხვი 2 სრულად რიცხვ1-ში. 

#105 , 16   6 ,  96 ნაშთი 9
num1= int(input("enter num1 bigger than 100:"))
num2= int (input("enter num2 between 10 and 20:"))

if num1 < 100 or num2 < 10 :  
    print ("You are dumb")
else:
    print (num1//num2)