def all_digits_even(num):
 for digit in str(num):
   if int(digit) % 2 != 0:
      return False
 return True
result = [num for num in range(1000, 3001) if all_digits_even(num)]
print("Numbers with all even digits between 1000 and 3000:", result)
