import random

number = random.Random().randint(1,50)

guess = 0
counter = 0
while guess != number:
    guess = int(input("Guess (1-50): "))
    if guess == number:
        print("Felicitari! Ai ghicit in " + str(counter) + " incercari!!!")
    elif guess > number:
        print("Felicitari! Numarul este mai mic!")
        counter += 1
    elif guess < number:
        print("Felicitari! Numarul este mai mare!")
        counter += 1