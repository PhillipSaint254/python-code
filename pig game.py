import random
computer= (random.randint(1,100))

while True:
    choice=input("enter a number between 1 and 100")
    if choice==computer:
        print("congratulations you guessd the number correctly")
    else:
        print("you lost")

    break