flag = 0
for i in range(3):
    u_n = input()
    pas = input()
    if(u_n != 'Micheal'):
        print("invalid username")
    elif (pas != 'e3$WT89x'):
        print("invalid password")
    else:
        flag=1
        print("you have successfully login")
        break
if (flag == 0):
    prin("account locked")
    
    # Your code doesnot have proper sequence, fix the bug
