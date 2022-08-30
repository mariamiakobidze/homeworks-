# # #fnctional 

# # #object oriented paradigm- OOP 

# # # algorithm 

# # # ა----ბ გზას ეწოდება ალგოირთმი 

my_nums = [15, 6, 20, 3]

# # #როგორ დავადგიო რომელიაყველაზე დიდი რიცხვი ამ სიაში რა არის აქ ალგორითმი 

# # # ვიღებთ სიის პირველ ელემენტს: 15-ს  შედარდეს 6, 20, 3 
# # შემდეგ 20 აშევადარებთ ანუ 
# # 20 ალგორითმი 


# # რა არის პროგრამირებაში ფუნქცია 
# #ფუნქცია არის ალგორითმი რომელიც არის reusable და გააჩნია სახლეი 

def my_multiplay(a, b): 
    print(a * b)
    
my_multiplay(5, 10)
my_multiplay(6, 16)
my_multiplay(16, 16)
my_multiplay(26, 16)


def create_khinkali(comis_type, shigtavsi):
  print("ჩემი ხინკალი არის",comis_type,
        "ცომისგან და მისი შიგთავსია:", shigtavsi)
comis_type= input("შეიყვანე ცომის ტიპი:")
shigtavsi = ("შეიყვანე შიგთავსის ტიპი:")
create_khinkali("თეთრი", "ყველი")
create_khinkali("რუხი", "კარტოფილი")









