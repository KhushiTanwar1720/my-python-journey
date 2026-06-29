import random
choices = ["Rock" ,"Paper" ,"Scissor"]
comp=random.choice(choices)
user=input("Enter Rock,Paper,Scissor").capitalize()
print(comp)
print(user)
if user=="Rock" and comp=="Scissor":
    print("Rock is winner")
elif user=="Scissor" and comp=="Rock":
    print("Rock is winner")
elif user=="Scissor" and comp=="Paper":
    print("Scissor is winner")
elif user=="Paper" and comp=="Scissor":
    print("Scissor is winner")
elif user=="Paper" and comp=="Rock":
    print("Paper is winner")
elif user=="Rock" and comp=="Paper":
    print("Paper is winner")
elif user==comp:
    print("Draw")
else:
    print("invalid input")