'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
count=0
while count<3:
    user_name=input("Enter the username: ")
    password =input("Enter the password:")
    if user_name =="Micheal" and password =="e3$WT89x":
    	print("You have successfully logged in")
    else:
        count+=1
        print("Invalid username and passwor")
        if count==3:
            print("Account Locked")
