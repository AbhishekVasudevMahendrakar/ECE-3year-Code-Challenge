#Write python code to verify user_name = "Micheal" and password ="e3$WT89x".
#The total number of attempts are 03.
# For every wrong user_name and password Print - Invalid username or Password, upon three attempts fails print- Account locked
#If inputs are correct Print - You have successfully login

attempt=0
while attempt<3:
	usr=input("Enter the username : ")
	pwd=input("Enter the password : ")
	if usr=="Micheal" and pwd=="e3$WT89x":
		print("Yoy have successfully logged in...")
		break
	else:
		attempt+=1
		print("Invalid username or password...\n")
		if attempt==3:
			print("Account locked...")

			# Very good your code is working fine
