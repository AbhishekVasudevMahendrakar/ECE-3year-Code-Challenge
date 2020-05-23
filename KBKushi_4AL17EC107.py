#Coding Challenge1
#K B Kushi - 4AL17EC107
#Write python code to verify user_name = "Micheal" and password ="e3$WT89x". The total number of attempts are 03. For every wrong user_name and password Print - Invalid username or Password, upon three attempts fails print- Account locked
#noOfAttempts is a variable to intialize the no of attempts mnade i  order to limit the entry to 3
noOfAttempts = 0
#here the while loop runs for 3 iterations
while noOfAttempts < 3:
    #username and password are two string variables which take input of the username and password 
    username = input("Enter username: ")
    password = input("Enter password: ")
    #the primary condition checks if the username and password entered is right comparing with respect to the credentials 
    if username=="Micheal" and password=='e3$WT89x':
        #if true it prints the below message 
        print('Logged in successfully')
        break
    else:
        #if false it prints as beloew
        print('Invalid Username or password. Try again.')
    noOfAttempts = noOfAttempts + 1
        #if the number of attempts exceeds 3 it prints the message below
    if noOfAttempts == 3 :
        print("Account Locked")
