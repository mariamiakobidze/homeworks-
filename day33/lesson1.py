#დათვლა კონკრეტული ასოსი ან ნიშნის კონკრეტულიად ' @' -სი 

my_str = ' G@e @Lagnol @idz@e'

print(my_str.count(' @'))

#დაჯამებასავით 
sum =1 
counter = 0

for i in range(5):
    x= 0 
    if x<1:
        sum += i
        counter += i
        x+= 1
        
    else:
        break
print(sum + counter)
  
# უჯიშო ასო ცვლილება მაგ: Xachiapuri და აშშ დაგიპრინტავთ 

import random 

my_chars = "shiqwndqjiedinwif"
my_str = "Xachapuri"
new_str = my_str.replace(my_str[ random.randint(1, len(my_str )-1) ], random.choice(my_chars))  
print(new_str)


