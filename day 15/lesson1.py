# #ჰკითხეთ მომხმარებელს სახელი და ეკრანზე გამოიტანეთ შეტყობინება, 
# #"გამარჯობა, saxeli"

# #გააკეთეთ format ფუნქციით

# user_name = input("whats your name: ")

# print("greetings {}".format(user_name))
# #N2 
# num1= input("Your first num:")
# num2= input("Your second num:")
# sum_num = int(num1 ) + int(num2)
# print (sum_num)
# #N3 N 2 but diff way 
# num1=int (input("enter num1:"))
# num2= int (input("enter num2 :"))
# sum_of_nums = num1 + num2 
# print ("{}+{}={}" .format (num1, num2, sum_of_nums))
#N4 
# num1=int (input("enter num1:"))
# num2= int (input("enter num2 :"))
# num3= int (input("enter num3 :"))
# num4= int (input("enter num4 :"))
# sum_of_squares_of_nums = num1*num1 +num2* num2+ num3*num3+ num4 *num4/ num1+num2+num3+num4 
# print ("{}*{}*{}*{}*{}*{}*{}*{} / {}+ {} + {}+ {}={}" .format (num1,num1,num2,num2,num3,num3,num4,num4,num1,num2,num3,num4, sum_of_squares_of_nums))
# #N5 
# # მომხმარებელს შემოატანინეთ ოთხი რიცხვი და გამოიტანეთ ეკრანზე მათი კვადრატების ჯამი გაყოფილი მათ ჯამზე.

# #მაგალითად, 2, 3, 5, 6

# #  (22 + 33 + 55 + 66 ) /  (2+3+5+6) =


# num1 = int(input("enter num1: "))
# num2 = int(input("enter num2: "))
# num3 = int(input("enter num3: "))
# num4 = int(input("enter num4: "))

# sum_of_squares_of_nums = (num1 * num1 + num2 * num2 + num3 * num3 + num4 * num4)

# print(sum_of_squares_of_nums / num1 + num2 + num3 + num4)
#N6 
x= int(input("How many slices does pizza have:"))
y= int(input ("How many slices of pizza did you eat:"))
z= int (x-y)
print ("{}ნაჭრიან პიცაში {}ნაჭერი შეიჭამა დარჩა{}ნაჭერი".format(x,y,z))
#N7
 #მომხმარებელს შემოაქვს ორი ცვლადი  1) რამდენნაჭრიანი პიცაა 2) რამდენი ნაჭერი შეჭამა

# გამოიტანეთ წინადადების სახით, xნაჭრიან პიცაში შეიჭამა yნაჭერი და დარჩა zნაჭერი.


pizza_size = int(input("How many slices does pizza have:"))
slices_eaten = int(input("How many slices of pizza did you eat:"))
slices_left = int(pizza_size-slices_eaten)

print("{}ნაჭრიან პიცაში {}ნაჭერი შეიჭამა დარჩა{}ნაჭერი".format(
    pizza_size, slices_eaten, slices_left))
#N8 
guests = int(input("how many guests:"))
priece_of_food =int (input ("how much money did they spent:"))
print ("ერთ ადამიანს მოუწევს " + str(priece_of_food/guests) + "გადახდა")

