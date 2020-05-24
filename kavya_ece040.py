username = input("username: ")
password = input("password: ")

if password == 'e3$WT89x' and username == 'Micheal':
        print("you loged in succesfully")
count = 1
while count <3:
    if password != 'e3$WT89x' or username != 'Micheal':
        print("invalid username or password")
        count+=1
        username = input("username: ")
        password = input("password: ")
        if password == 'e3$WT89x' and username == 'Micheal':
            print("you loged in succesfully")
    if count==3:
        print("account locked")
        
        # your code is working fine, but after successful login it is not returning to shell command
            


