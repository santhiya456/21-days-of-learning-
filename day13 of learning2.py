s_username="Santhiya"
s_password="8300@"

uname=input("Enter a username:")
password=input("Enter a password:")

def validate():
    if(s_username==uname and s_password==password):
        return True
    else:
        return False

a=validate()
print(a)
