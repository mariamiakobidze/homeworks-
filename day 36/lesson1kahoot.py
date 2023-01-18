# N1 

def marto_saxlshi (santa, rudolfi): # ფუნქცია შევქმენით მარტო სახლში და გადავეცით რუდოლფი და სანტა 
    return abs(santa - 2 * rudolfi)# ვაბრუნებთ abs სანტას - 2 * რუდოლფზე 

print(marto_saxlshi(13, 7))# დაპრინტოს 13 და 7 ანუ სანტაა 13 და რუდოლფია 7 ( 13 - 2 * 7 = 1 )

#N 2
print("\tGOAL\nORI\nENTED\n\nACA\nDEMY\n") 

# N3

def gilocavt(num): # ფუნქცია გილოცავთ პარამეტრინ ნუმ აქ 4 გაეშვება და 
      if num == 0:  # თუ ნუმ = 0 დააბრუნოს 0 
          return 0
      else: # სხვა შემთხვევაში დააბრუნოს ნუმს - 1
          return gilocavt(num - 1) # 4 -1 უდრის 3 ანუ სამი ისევ დაბრუნდება if თან და დაიწყება ახლიდან სანამ num არ უდრის 0
        
n = gilocavt(4) # ნ უდრის გილოცავთ პარამეტრით 4

print(n) # დაპრინტოს ნ  ამას ქვია "რეკურსია" -_- 

#N4

def axali_weli(n): # ფუნქცია ახალი წელი პარამეტრით n
    if n <= -1: # თუ ნ ნაკლებია ან უდრის -1 
        return False # დააბრუნოს False
    elif n ** 0.5 % 1 == 0: # თუ n **0.5  % 1 == 0 (2023 ** 0.5 = 44.97777228809804)
        return True # დააბრუნოს True
    return False 

print(axali_weli(2023)) 


# N5 

import random # დავაიმპორტოთ რენდომი 

def random(x, y): # ფუნქცია რენდომი x y 
    return y - x - 3 # დააბრუნოს y - x - 3 

my_char = "abcefghijklmnopqrstuvwxyz" #მაი ჩარ ანბანი გადავეცით ცვლადს
my_str = input('Enter a word:')# gozinayi # მაი სტრ ცვლადს კიდევ ინფუთი
new_str = my_str. replace(my_str[random(1,len(my_str) - 1)], my_char[5])
#new str ცვლადს გადავეცით მაი სტრ repleace ბრძანებით
print(new_str) 

# N6

def dawere(my_str): # 
    print(my_str)
    
def xmas(str):
    new_str = ''
    for char in my_str:
        if char.isupper():
            new_str += char.lower()
        else:
            new_str += char.upper()
    return new_str

my_str = 'SnoViM GoOd Am'
dawere((xmas(my_str)))


#N7

import random

def mde(num): 
    d_sum = 1
    counter = 0
    while len(str(num)) != 1:
        for d in str(num):
            d_sum *= int(d)
            num = d_sum
        d_sum = 1
        counter += 1 
    return counter + d_sum 
print(mde(39))



