# list = [1,2,3,4,5,6,7,8,9]

# print(sum(list))

# list = [1,2,3,4,5,6,7,8,9]

# sum = 0 

# for number in list:
#     sum += number 
    
# print(sum)


# nums = list(range(5))
# print(nums[4])

# print((4 * 8) / 2)

# print(60 +1 )

# numbers = list (range (3,15,3))

# print (numbers)

# nums = list(range(5,8))
# print(len(nums))


# numbers = list(range(2005,2011))

# print(numbers)

# a = int(input())
# b = int(input())

# my_list=[]

# for i in range(a,b):
#     my_list.append(i)
    
# print(my_list)


# list = [1,1,2,3,5,8,13]

# print(list[list[4]])

# def rps(p1, p2 = (str(input()))):
#     if p1 == p2:
#         return 'Draw!'
#     if (p1 == 'rock' and p2 == 'scissors') or (p1 == 'scissors' and p2 == 'paper') or (p1 == 'paper' and p2 == 'rock'):
#         return 'Player 1 won!'
#     else:
#         return 'Player 2 won!'

# list_num = list((range)(abs(-3),7))

# print(list_num)

# greeting = input("")

# for char in greeting:
    
#     print ("char + !")
    
# a = [4,1,2,3]
# b = list(range(1,6,2))

# for i in a:
#     b.append(a[i+1] + a[i])
    
# print (b)



import random

attempts_list = []

def show_score():

   if len(attempts_list) <= 0:

    print("There is currently no high score, it's yours for the taking!")

   else:

    print("The current high score is {} attempts".format(min(attempts_list)))

def start_game():

    random_number = int(random.randint(1, 10))

    print("Hello traveler! Welcome to the game of guesses!")

player_name = input("What is your name? ")

wanna_play = input("Hi, {}, would you like to play the guessing game? (Enter Yes/No) ".format(player_name))

# Where the show_score function USED to be

attempts = 0

show_score()

while wanna_play.lower() == "yes":

   guess = input("Pick a number between 1 and 10 ")

if int(guess) < 1 or int(guess) > 10:

    raise ValueError("Please guess a number within the given range")

random_number = []

if int(guess) == random_number:

    print("Nice! You got it!")

attempts += 1

attempts_list.append(attempts)

print("It took you {} attempts".format(attempts))

play_again = input("Would you like to play again? (Enter Yes/No) ")

attempts = 0

show_score()

random_number = int(random.randint(1, 10))

if play_again.lower() == "no":

   print("That's cool, have a good one!")


elif int(guess) > random_number:

    print("It's lower")

attempts += 1

if int(guess) < random_number:

   print("It's higher")

attempts += 1

if ValueError:

    print("Oh no!, that is not a valid value. Try again...")

err = []

print("({})".format(err))

print("That's cool, have a good one!")

__name__ == '__main__'
  
start_game() 