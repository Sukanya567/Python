n= input("Enter a 4-digit number: ")
if len(n) == 4 and n.isdigit():
    even_digits = []
    odd_digits = []
    for digit in n:
        if int(digit) % 2 == 0:
            even_digits.append(digit)
        else:
            odd_digits.append(digit)
    print("Even digits:", ", ".join(even_digits))
    print("Odd digits:", ", ".join(odd_digits))
    print("Total even digits:", len(even_digits))
    print("Total odd digits:", len(odd_digits))
else:
    print("Please enter a valid 4-digit number!")
