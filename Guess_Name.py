import random

names=["abhay","akshay", "amit", "anand","anil", "ansh", "arjun"]

name=random.choice(names)

flag=True
chances=1
while flag:
    guess= input("Enter name: ").lower()
    if name==guess:
        print("you guessed it right!!")
        flag=False
    elif chances==5:
        print("\nSorry you lost :(")
        break
    else:
        print("Try again buddy")
        chances+=1

        










