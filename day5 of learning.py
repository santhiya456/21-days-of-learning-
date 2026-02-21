age=int(input("Enter your age:"))
gender=input("Enter your gender(male/female):")
if(age>=18):
    if(gender=="male"):
        print("Eligible male voter")
    elif(gender=="female"):
        print("Eligiblr female voter")
    else:
        print("Gender not recognized")
else:
    print("Not eligible to vote")
