import random
cnumber=(random.randint(1,500))
userInput=int(input("Enter Your Number:--- "))
print("Computer Number is:--  ",cnumber)
if(userInput==cnumber):
    print("Number is Equal")
elif(userInput>cnumber):
    print("Guessing Number is Too High ")
else:
    print("Guessing Number is Too Low")