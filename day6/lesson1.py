# 1) list
# 2) tuple  (1,2,3,10,20)
# 3) set 
# 4) dictionary 


1
my_list = [1,2,3,10,20]  #სიაში შეგვიძლია ყველაფრის გაკეთება

my_list.append(15)
my_list.insert(2,15)

print(my_list)

2 
my_tuple = (1,2,3,10,20)  #tuple ტიპის სიაში, არ შეგვიძლია ცვლილებების განხორციელება
my_tuple[3] = 12

3
my_set = {1, 2, 2}   #სეთში არ შეიძლება იყოს ერთი და იგივე ელემენტები
print(my_set)

4
my_dict = {"name":"nika",
           "surname": "keshelava",
           "age": 22,
           "hobbies" : ["programming", "psychology", "art", "music", "gym_beast", "aguri"]
           }

print(my_dict["surname"])
print(my_dict["hobbies"][0])

for hobby in my_dict["hobbies"]:
    if hobby[0] == "p":
        print(hobby, "starts with p")

print(5 == 10)
print(5 != 10)
print(10>5)
passwords_dict = {
    "nika"
}

passwords = ["memiyvarsdediko123", "aguri", "paroliparoli", "memiyvarsmamiko123", "shaurma"]

users_input = input("enter your password: ")

if users_input in passwords:
    print("your password is in our server")
else:
    print("i don't know you, please register :)) ")


passwords_data = {
    "nika123" : "aguri",
    "giohackera" : "berlin123",
    "aguri2": "aguri3",
    "nikagamer123": "nika12345",
    "lukatmg" : "gaymer",
    "tvimedi" : "youtubeisdangerous",
    "pubgfan" : "iamgay",
    "forniteissobad" : "minecraftisbetter",
    "dota2" : "iamchad",
    "leagueoflegends" : "dota2tutorial"
}

username = input("welcome, enter your username: ")

if username in passwords_data:
    print("okay, now time for the password")
    password = input("enter your password: ")

    for key in passwords_data.keys():  #ციკლი მთლიან ბაზაში
        if key == username:   #ვამოწმებთ თუ გასაღები უდრის შეყვანილ იუზერნეიმს
            if password == passwords_data[username]:  #ვამოწმებთ თუ შეყვანილი პაროლი უდრის რეალურ პაროლს
                print("successfully login")
            else:
                print("invalid password")

else:
    print("please register")