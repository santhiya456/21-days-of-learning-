class student:
    def __init__(self, name):
        self.name=name

    def result(self):
        total=0
        for i in range (3):
            mark=int(input("Enter mark:"))
            total+=mark

        avg=total/3
        print("Name:",self.name)
        print("Total:",total)
        print("Average:",avg)

        if avg>=50:
            print("Pass")
        else:
            print("Fail")


s=student("Santhiya")
s.result()
