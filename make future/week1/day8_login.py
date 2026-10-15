#ACCING THE USER(LOGIN):
username = input("Enter your username: \n")
password = input("Enter your password: \n")
if username != 'admin' and password !='python123':
    print("access denied")  

else:
    print("access granted")