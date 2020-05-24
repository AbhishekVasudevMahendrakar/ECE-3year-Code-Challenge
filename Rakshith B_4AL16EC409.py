attempt=0
while attempt<3:
    input1=input("enter the username : ")
    input2=input("enter the password : ")
    if input1=='Micheal' and input2=='e3$WT89x':
        print('loggedin Successfully')
        break
    else :
        print('invalid username or password')
        attempt+=1
if attempt==3:
    print("account locked")
    
    # Very good, your code is fine
