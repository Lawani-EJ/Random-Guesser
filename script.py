import random

guessed_answer = random.randrange(1, 101)
life = 0
print("Hello and Welcome to the Guess the Number game!")
print("Guess the correct number and win the Game")
print("NOTE!!!!!!!!!!!!!!!")
print("You Only Have 5 lives")

while life < 5:
    guess_number = int(input("Guess a number from 1 to 100 "))
    if guess_number == guessed_answer:
        print("Congratulations You guessed the right answer")
        break
    if guess_number > guessed_answer:
        print("Your guess is too high use a lower number")
    elif guess_number < guessed_answer:
        print("Your guess is too low use a higher number")

    life += 1

    if life == 5:
        print("Game Over!!!!")
        print("The number was", guessed_answer)
        break

