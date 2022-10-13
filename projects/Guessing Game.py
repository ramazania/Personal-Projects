import random

print("Welcome to the guessing game! \n")
isTrue = False
number = random.randint(0, 100)
count = 0

userInput =  int(input("Guess a number between 0 - 100: "))

while isTrue == False:
    if (userInput < 0 or userInput > 100) :
        print("Out of range! ")
        userInput =  int(input("Try again: "))
    else:
            if userInput > number:
                count += 1
                print("Too high!")
                userInput =  int(input("Try again: "))
            elif userInput < number:
                count += 1
                print("Too low!")
                userInput =  int(input("Try again: "))
            else:
                count += 1
                print("you got it! Total attems: " , count)
                isTrue = True







