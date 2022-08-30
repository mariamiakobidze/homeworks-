#N1 რა შედეგს გამოიტანს ტერმინალში ?
def secret_code (s): # ვქმნით ფუნქციას პარამეტრით s
    splitted_arr = s.split(" ") # ცვლადი Splitted_arr(დაყოფილი სია) და ვეუბნებით 
    #რომ splitით დავყოთ " " სადაც სპეისებია
    splitted_arr.reverse() # ვეუბნებით რომ ეს სია შემოატრიალოს
    
    my_str = "" # ვქმნით ცარიელ სტრინგს სხელდ my_str

    for element in splitted_arr: # ელემენტისთვის ამ სიაში 
        my_str += element  # ჩემს სტრინგს დაემატოს ეს ელემენტი
        my_str += " "  # და სტრინგს დავუმატოთ სფეისები
        
    return my_str [:-1]# დააბრუნოს სტრინგი -1 მდე

print(secret_code("hello world 23")) # დაპრინტოს ფუნქცია პარამეტრი "hello world 23" ით 
# 23 world hello დაიპრინტება 


#N2 რა შედეგს გამოიტანს ტერმინალში?
def secret_code (s):# ვქმნით ფუნქციას პარამეტრით s
    splitted_arr = s.split (" ")# ცვლადი Splitted_arr(დაყოფილი სია) და ვეუბნებით 
    #რომ splitით დავყოთ " " სადაც სპეისებია
    splitted_arr.reverse() # ვეუბნებით რომ ეს სია შემოატრიალოს
    
    my_str = "" # ვქმნით ცარიელ სტრინგს სხელდ my_str
    
    for element in splitted_arr: # ელემენტისთვის ამ სიაში
        my_str += element # ჩემს სტრინგს დაემატოს ეს ელემენტი
        my_str += " "  # და სტრინგს დავუმატოთ სფეისები
        
    return my_str[:-1]# დააბრუნოს სტრინგი -1 მდე

print(secret_code("hello world 2 3")) # დაპრინტოს ფუნქცია პარამეტრი "hello world 2 3" ით 
# 3 2 world hello დაიპრინტება 


#N3 
def smash(words): # ვქმნით ფუქციას smash და პარამეტრად გადავცემთ word-ს
    my_str = "" # ვქმნით ცვლადს ცარიელ სტრინგ my_str(ჩემი სტრინგი)-ს
    for element in words:# ელემენტისთვის word ში 
        my_str += element #ჩემს სტრინგს დავუმატოთ ელემენტი
        my_str += " " # და ჩემს სტრინგს დავუმატოთ space
        
    return my_str [:-1]# დააბრუნოს my_str -1 ამდე 

print(smash("hello friend"))# დაპრინტოს ფუნქცია პარამეტრით "hello friend"
# დაიპრინტება h e l l o f r i e n d


#N4 რა შედეგს გამოიტანს ტერმინალში?
def grow(arr):# შევქმენით ფუნქცია grow და გადავეცით პარამეტრი arr
    product_of_nums = 1 # შევქმენით ცვდადი product_of_nums და ის უდრის 1 
    for element in arr: # ელემენტისთვის სიაში 
        product_of_nums *= element # ცვლადი გავამრავლოთ ელემენტზე
        
    return product_of_nums # დააბრუნე ცვლადი 

print(grow(10,20,3)) # გამოიძახოს ფუნქცია gorw პარამეტრებით 10,20,3
# ამოაგდებს erros- ს რადგან () ამ ფრჩხილის მაგივრად უნდა იყოს [] ეს ფრჩხილები 


#N5 რა შედეგს გამოიტანს ტერმინალში?
def grow(arr):# შევქმენით ფუნქცია grow და გადავეცით პარამეტრი arr
    product_of_nums = 1 # შევქმენით ცვდადი product_of_nums და ის უდრის 1 
    for element in arr: # ელემენტისთვის სიაში 
        product_of_nums *= element # ცვლადი გავამრავლოთ ელემენტზე
        
    return product_of_nums # დააბრუნე ცვლადი 

print(grow([10,20,3,2]))# გამოიზახოს ფუნქცია 
# დაიპრინტება 1200


#N6 რა შედეგს გამოიტანს ტერმინალში ? 
def better_than_avarage(class_points, your_points): # შევქმენით ფუნქცია და გადავეცით 2 პარამეტრი

    sum_of_points = sum(class_points) # შევქმენით ცვლადი 
    ammount_of_students = len(class_points)# შევქმენით მეორე ცვლადი 
    
    avarage_score = sum_of_points/ ammount_of_students # შევქმენით მესამე ცვლადი 
    #სადაც პირველ ორ ცვლადს ერთმანეთზე ვყოფთ 
    if your_points > avarage_score: # ვქმნით ციკლს თუ ჩემი ქულები მეტია საშუალო ქულაზე 
        return True # დაგვიბრუნდება True 
    elif your_points <= avarage_score:# თუ ჩემი ნიშანი ნაკლებია ან ტოლია საშუალო ქულის 
        return False # დაგვიბრუნდეს Flase 
    
better_than_avarage([10,20,15,],14) # ვიძახებთ ფუნქციას და გადავცემთ პირველის პარამეტრად[10,20,15]
# ხოლო მეორის 14 მაგრამ არ დაიპრინტება არაფერი რადგან არ გვაქვს print 87 ხაზზე 


#N7 რა შედეგს გამოიტანს ტერმინალში ?
def better_than_avarage(class_points, your_points): # შევქმენით ფუნქცია და გადავეცით 2 პარამეტრი

    sum_of_points = sum(class_points) # შევქმენით ცვლადი 
    ammount_of_students = len(class_points)# შევქმენით მეორე ცვლადი 
    
    avarage_score = sum_of_points/ ammount_of_students # შევქმენით მესამე ცვლადი 
    #სადაც პირველ ორ ცვლადს ერთმანეთზე ვყოფთ 
    if your_points > avarage_score: # ვქმნით ციკლს თუ ჩემი ქულები მეტია საშუალო ქულაზე 
        return True # დაგვიბრუნდება True 
    elif your_points <= avarage_score:# თუ ჩემი ნიშანი ნაკლებია ან ტოლია საშუალო ქულის 
        return False # დაგვიბრუნდეს Flase 
    
print(better_than_avarage([10,20,15,],16)) # ვიძახებთ ფუნქციას პირველის პარამეტრებია [10,20,15]  ხოლო მეორის 16 
# დაიპრინტება True რადგან (10+20+15)/3= 15 ხოლო 16>15

#N8 რა დაიპრინტება?
our_list = ["nika""gio","gabrieli","saba","and others"]# შევქმენით ჩვენი სია 4 ელემენტით 

i = -1  # ცვლადი -1 

for char in our_list: # ასოებისთვის ჩვენს სიაში
    for char in our_list:# ასორებისთვის ჩევენს სიაში
        i -=2 # გაგრძელდეს სანამ i -=2 
        
# დაიპრინტება არაფერი რადგან არ გვაქვს print 

#N9 რა დაიპრინტება?
our_list = ["nika""gio","gabrieli","saba","and others"]# შევქმენით ჩვენი სია 4 ელემენტით 

i = -1  # ცვლადი -1 

for char in our_list: # ასოებისთვის ჩვენს სიაში
    for char in our_list:# ასორებისთვის ჩევენს სიაში
        i -=2 # გაგრძელდეს სანამ i -=2 
        
print(i) # დაპრინტავს -33 
        
#N10 რას დაპრინტავს?
our_list = ["nika""gio","gabrieli","saba","and others"]# შევქმენით ჩვენი სია 4 ელემენტით 

i = -1  # ცვლადი -1 

for char in our_list: # ასოებისთვის ჩვენს სიაში
    for char in our_list:# ასორებისთვის ჩევენს სიაში
        i *=2 # გაგრძელდეს სანამ i *=2 
    
print(i)# დაიპრინტება -65536~

#N11რა დაიპრინტება?~
our_list = ["nika""gio","gabrieli","saba","and others"]# შევქმენით ჩვენი სია 4 ელემენტით 

i = -1  # ცვლადი -1 

for char in our_list: # ასოებისთვის ჩვენს სიაში
    for char in our_list:# ასორებისთვის ჩევენს სიაში
        i +=4 # გაგრძელდეს სანამ i +=4
    
print(i)# დაიპრინტება 63 

#N12 რა დაიპრინტება?
our_list = ["nika""gio","gabrieli","saba","and others"]# შევქმენით ჩვენი სია 4 ელემენტით 

i = 1  # ცვლადი 1 

for char in our_list: # ასოებისთვის ჩვენს სიაში
    for char in our_list:# ასორებისთვის ჩევენს სიაში
        i +=1 # გაგრძელდეს სანამ i +=1
    
print(i)# დაიპრინტება 17





