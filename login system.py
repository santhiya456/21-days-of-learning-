username=input("Enter username:")
password=input("Enter password:")

correct_user=(username=="Admin")
correct_pass=(password=="12345678")

print("username:",correct_user)
print("Password:",correct_pass)

if(correct_user and correct_pass):
    print("Login successful")
else:
    print("Login failed")
