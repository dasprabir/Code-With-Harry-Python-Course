import random

randNo = random.randint(1,3)

if randNo == 1 :
    comp = 's'
elif randNo == 2:
    comp = 'w'
else : 
    comp = 'g'

def gameWin(comp,you) :
    if comp == you :
        return  None
    if comp == 'g' :
        if you == 's' :
            return False
        else  :
            return True
    elif comp == 'w' :
        if you == 's' :
            return True
        else  :
            return False
    elif comp == 's' :
        if you == 'g' :
            return True
        else  :
            return False



you = input("Enter snake(s) or water(w) or gun(g) :")
print("Computer chose "+comp)

f = gameWin(comp,you)

if f == None:
    print("Tie !!!")
elif f == True :
    print("You Win!!!")
else :
    print("You Loose!!!")

