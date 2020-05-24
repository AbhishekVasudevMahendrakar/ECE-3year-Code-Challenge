print('Enter correct username and password  to continue')
count=0
while count < 3:
    username = input('Enter username: ')
    password = input('Enter password: ')
    if password=='e3$WT89x' and username=='Micheal':
        print('login successful')
        
    else:
         count += 1
         print('Incorrect username/password.Try again')
         
        
    if count==3:
        print('Account locked.' )
        
        # your code has bug, after successful login, again it is asking for credentials
        Enter correct username and password  to continue
Enter username: Micheal
Enter password: e3$WT89x
e3$WT89x
login successful
Enter username: 
