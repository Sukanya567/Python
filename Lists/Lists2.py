n = input("Enter a 10-digit number: ")
if len(n) == 10 and n.isdigit():
    max_digit = max(n)
    print("The digit with the maximum value is:", max_digit)
else:
    print("Please enter a valid 10-digit number!")
