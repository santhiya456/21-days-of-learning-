request_count = int(input("Enter number of requests: "))

limit = 5

if request_count <= limit:
    print("Status: Allowed")
else:
    print("Status: Blocked (Rate Limit Exceeded)")
    
