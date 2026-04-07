import random
number=random.randint(1,10)
guess = int(input("guess a number between 1 to 10:"))
if guess == number:
   print("correct!you guessed it right")
else:
   print("wrong!the number was:",number)
