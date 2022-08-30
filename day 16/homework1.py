#დავალება!!!
#მომხმარებელს შემოატანინეთ სიტყვა და დაითვალეთ ცალკე ხმოვნების რაოდენობა, ცალკე - თანხმოვნების. 

#გამოიტანეთ გრძელი წინადადება, წინის მსგავსად.

sityva = input("chaweret tqveni sityva: ")
xmovan_counter = 0
tanxmovani_counter = 0 
for char in sityva:
    if char in "aeiouAEIOU":
        xmovan_counter += 1 
        
for char in sityva:
    if char in "qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM":
        tanxmovani_counter +=1

print(sityva+ "-shi " + str(xmovan_counter) + " xmovania"+"da"+ str(tanxmovani_counter)+ "tanxmovania") 