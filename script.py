# Random Guesser 
print("Hello and Welcome to the Guess the Number game!")
import random
guess = (random.randint(1,100))
print("Hello and welcome to the Guess the Number game!")
print("I'm thinking of a number between 1 and 100. Can you guess what it is?")
my_number = int(input("Enter Your NUmber Here: "))
if guess > my_number:
    print("Your Number is too Low")
elif guess < my_number:
    print("Your Number is High")
else:
    print("Your Number is Correct")

while guess != my_number:
   my_number =  int(input("Enter the guessed Number Here => "))
   if my_number == guess:
       print("Congratulations You guessed the right answer2")