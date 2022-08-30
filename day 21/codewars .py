def simple_multiplication(number) :
    if number % 2 ==0 :
        return number * 8
    else:
        return number * 9 
    
def zero_fuel(distance_to_pump, mpg, fuel_left):
    if distance_to_pump <= mpg * fuel_left:
        return True 
    else :
        return False
    
def are_you_playing_banjo(name):
    if name[0]== "r" or name[0]== "R":
        return name + " plays banjo"
    else: 
        return name + " does not play banjo"
    
def hero(bullets, dragons):
    if bullets  >= dragons *2:
        return True 
    else: 
        return False 
    
def check(seq, elem):
    if elem in seq:
        return True
    else:
        return False 
    
def multiply(a, b):
    return a*b

def string_to_array(s):
    return s.split(" ")

def bmi(weight, height):
    bmi = weight / height **2
    if bmi <= 18.5: 
        return "Underweight"
    if bmi <= 25.0:
        return "Normal"
    if bmi <= 30.0:
        return "Overweight" 
    else:
        return "Obese"
    
def DNAtoRNA(dna):
    return dna.replace('T', 'U')

def grow(arr):
    num = 1 
    for i in arr:
        num *= i 
        
    return num

def reverse_words(s):
    return " ".join(s.split(" ")[::-1])

def count_by(x, n):
    arr = []
    for i in range (1, n + 1):
        arr.append (i * x)
    return arr

#Grasshopper - Grade book

def get_grade(s1, s2, s3):
    m = (s1 + s2 + s3) / 3.0
    if 90 <= m <= 100:
        return 'A'
    elif 80 <= m < 90:
        return 'B'
    elif 70 <= m < 80:
        return 'C'
    elif 60 <= m < 70:
        return 'D'
    return "F"

#1If you can't sleep, just count sheep!!
def count_sheep(n):
    if n == 1:
        return "1 sheep..."
    else:
        return count_sheep(n - 1) + "{} sheep...".format(n)
#2Rock Paper Scissors!
def rps(p1, p2):
    if p1 == p2:
        return 'Draw!'
    elif (p1 == 'rock' and p2 == 'scissors') or (p1 == 'scissors' and p2 == 'paper') or (p1 == 'paper' and p2 == 'rock'):
        return 'Player 1 won!'
    else:
        return 'Player 2 won!'
        
#3Total amount of points
def points(games):
  # good solution without condition ))))
  count = 0
  for i in games:
      if int(i[0]) > int(i[2]):
          count += 3
      elif int(i[0]) == int(i[2]):
          count += 1
      
  return count
#4Quarter of the year
def quarter_of(month):
    if month in (1,2,3):
        return 1
    elif month in (4,5,6):
        return 2
    elif month in (7,8,9):
        return 3
    elif month in (10,11,12):
        return 4
#5
def monkey_count(n):
    list = []
    for i in range(1,n+1):
        list.append(i)
    return list

def monkey_count(n):
    return range(1, n+1)
#6Sum Mixed Array
def sum_mix(arr):
    sum = 0
    for number in arr:
        sum += int(number)
    return sum

#7Sum without highest and lowest number

#8
def remove_exclamation_marks(s):
    return s.replace('!', '')
#9Do I get a bonus?
def bonus_time(salary, bonus):
    #your code here
    if bonus :
        return "$" + str(salary * 10)
    else:
        return "$" + str(salary)
#10set alarm 
def set_alarm(employed, vacation):
    if employed and vacation is False:
        return True
    else:
        return False

#11Beginner Series #4 Cockroach
def cockroach_speed(s):
    return s * 100000 // 3600

#12Grasshopper - Check for factor
def check_for_factor(base, factor):
    return True if base%factor == 0 else False


