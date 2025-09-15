import random
num=int(random.random()*100)

flag=True
chance=0
while flag:
    b = int(input("num: "))
    if b==num:
        print("You got it!!")
        flag=False
    elif b<num:
        print("You are low")
        chance+=1
    else:
        print("You are high")
        chance+=1
        
    if chance==5:
        print("you lost")
        break;
        
