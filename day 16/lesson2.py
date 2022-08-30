# arr = ["nika", "nika1", "nika2"]

# i = ""

# for element in arr:
#     for char in element:
#         i+= char 

# print(i)

# arr = ["nika", "nika1", "nika2"]

# i = 0
# final_str = ""

# for i in range(3):
#    if i==0:
#     final_str += "nika"
#    if i> 0:
#     final_str += "nika" + str(i)
    
    

# print(final_str)

# # num1 = str(input("enter girl name: ")) 
# # num2 = str(input("boy name: "))

# # print("{} + {} = {}".format(num1, num2))



# card_nums = "5318 1812 8182 0075"
# dafaruli_nums= "#### #### #### ####"

# print (dafaruli_nums[:-4])


card_nums = "5318 9873 9821 0075"



temp_str = ""
i = 1
while i <= len(card_nums)-4:
    if i % 5 != 0:
         temp_str += "#"
    else:
        temp_str += " "
    i+= 1
    
temp_str += card_nums[-4:]

print(temp_str)
         
