post = input("Enter your post : ")

if 'Harry' or 'harry' or 'HaRRy' or 'HArry' or 'HarrY' or 'HARRY' in post :
    f = True
else :
    f = False

if(f) :
    print("Talking about Harry !!!")
else :
    print("NOT Talking about Harry !!!") 
