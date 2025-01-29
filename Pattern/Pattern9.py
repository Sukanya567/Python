n = int(input('Enter the number:'))
rx = n // 2 + 1
for x in range(1, n + 1):
  for y in range(1, n + 1):
    if y == rx or y == n - rx + 1:
       print("*", end="")
    else:
       print(" ", end="")
  if x <= n // 2:
     rx -= 1
  else:
     rx +=1
  print()
