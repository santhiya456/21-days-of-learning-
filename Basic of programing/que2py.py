total_messages = int(input("Enter total messages: "))

if total_messages <= 100:
    active = total_messages
    compressed = 0
    status = "Normal"
else:
    active = 100
    compressed = total_messages - 100
    status = "Optimized"

print("Status:", status)
print("Active:", active)
print("Compressed:", compressed)


