name=input("Enter your name:")
age=int(input("Enter your age:"))
citizen=input("Are you a citizen(Yes/no):")

is_adult=age>=18
is_citizen=(citizen=="yes")

print("Name:",name)
print("Age:",is_adult)
print("Citizen:",is_citizen)

if(is_adult and is_citizen):
    print("Eligible to vote")
else:
    print("Not eligible to vote")
