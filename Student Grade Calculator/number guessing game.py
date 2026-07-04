import random
secret_number = (random.randrange(1, 100))
attempts = 0
while True:
 guess = int(input("Enter your guess:"))
 attempts+=1
 if guess > secret_number:
    print("To High")
 elif guess < secret_number:
      print("To Low")
 else:
    print("correct")
    break
if False:
    print("invalid input")