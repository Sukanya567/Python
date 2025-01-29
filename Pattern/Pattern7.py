n = int(input('Enter the number:'))
for x in range(n):
   rx = 1
   print(" " * (n - x), end="")
   for y in range(x + 1):
       print(rx, end=" ")
       rx = rx * (x - y) // (y+1)
   print("")
