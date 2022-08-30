#N1 
# მომხმარებელს ფუნქციაში შეყავს 2 რიცხვი უნდა დააბრუნოს X მეტია y ზე z ით 
#მაგალითად:
# პირველი რიცხვი 10 
# მეორე რიცხვი 35 
# output: 35 მეტია 10 ზე 25 ით 


x = int(input("enter X:"))
y = int(input("enter Y: "))

def comparision_of_nums (x,y): 
     if x>y:
         return "x მეტია y-ზე " + str(x-y) + "ით"
     elif y>x :
         return "y მეტია x- ზე" + str(y-x) + "ით"
     
print(comparision_of_nums(x, y))
        
         
        
    
   
























