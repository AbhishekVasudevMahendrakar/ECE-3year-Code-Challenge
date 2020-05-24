#bug fixed 
for i in range(1,4):
    u_n = input("Enter username: ")
    pas = input("Enter Password: ")
    if(u_n == 'Micheal' and pas  == 'e3$WT89x' ):
        print("You have successfully login...")
        break
    else :
        print("Invaid username or password...")
        if(i == 3):
            print("Account Locked...")
