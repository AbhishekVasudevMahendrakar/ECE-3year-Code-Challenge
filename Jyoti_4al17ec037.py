attempt=0
while attempt<3:
    user_name=input("enter the username:")
    password=input("enter the password:")
    if user_name=="Micheal" and password=="e3$WT89x":
        print("you have successfully logged in")
    else:
        attempt+=1
        print("invalid username or password")
print("account locked")

# your code has bug, after successful login, again it is asking credentials
enter the username:Micheal
Micheal
enter the password:e3$WT89x
e3$WT89x
you have successfully logged in
enter the username:sd
sd
enter the password:
