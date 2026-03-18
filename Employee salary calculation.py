name=input()
salary=int(input())

bouns=salary*0.10
total_salary=salary+bouns

print("Name:",name)
print("Salary:",salary)
print("Bouns:",bouns)
print("Total salary:",total_salary)

if(total_salary>80000):
    print("High salary")
else:
    print("Normal salary")
              
