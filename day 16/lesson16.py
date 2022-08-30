# my_name = "Mari"
# print (len(my_name))

# word = input ("enter word:")
# first= word[0]
# rest = word[1:len(word)]
# final_str = ""
# if first not in "aeiou":
#     final_str += rest + first +"ay"
# else:
#     final_str += "debilobana"
    
# print(final_str)




sityva = input("chaweret tqveni sityva: ")
xmovan_counter = 0
for char in sityva:
    if char in "aeiouAEIOU":
        xmovan_counter += 1 

print(sityva+ "-shi " + str(xmovan_counter) + " xmovania")




