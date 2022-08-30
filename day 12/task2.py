# ფუნქციაში გადაეცით არგუმენტად რანდომ List 10 integer  დამიპრინტეთ 4 ის ჯერადები


import random # ვქმნით რენდომ ამრჩევს 


def jeradebi_4isa (my_list): 
    print(my_list) # ვპრინტავთ My_list 
    for element in my_list:
        if element % 4 == 0: # თუ 4 ზე გაყოფით ნაშთი არ გვაქვს 
            print (element,"არის 4 ის ჯერადი") # დაპრინტოს 4 ის ჯერადები 
    
my_list = [] # ვქმნით რენდომ მაი ლისთს 
for  i in range (10) : # რენდომ 10 რიცხვი 
    my_list.append(random.randint(1,50)) #რენდომ 10 იდან 50 ამდე 
    
jeradebi_4isa(my_list)
    
#Parse nice int from char problem
def get_age(age):
    return int(age[0])

#
def get_planet_name(id):
    planets = {
        1: "Mercury",
        2: "Venus",
        3: "Earth",
        4: "Mars",
        5: "Jupiter",
        6: "Saturn",
        7: "Uranus", 
        8: "Neptune",
    }
    return planets[id]
#Twice as old
def twice_as_old(dad_years_old, son_years_old):
    return abs(dad_years_old - 2*son_years_old)
#Will there be enough space?
def enough(cap, on, wait):
    return max(0, wait - (cap - on))
#Switch it Up!
def switch_it_up(n):
    return ['Zero','One','Two','Three','Four','Five','Six','Seven','Eight','Nine'][n]
#The Feast of Many Beasts
def feast(beast, dish):
    return beast[0] == dish[0] and beast[-1] == dish[-1]
#Removing Elements
def remove_every_other(my_list):
    return my_list[::2]




