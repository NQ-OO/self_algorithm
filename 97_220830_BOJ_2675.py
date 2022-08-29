
for i in range(int(input())) : 
  r, s = input().split()
  p = [int(r)*single_char for single_char in list(s)]
  print("".join(p))

