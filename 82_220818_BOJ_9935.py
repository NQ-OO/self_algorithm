import sys

input = sys.stdin.readline

str_lst = list(input().strip())
bomb = input().strip()

stack = []

for single_char in str_lst :
  stack.append(single_char)
  if len(stack) >= len(bomb) :
    if (stack[-1] == bomb[-1]) and ("".join(stack[-(len(bomb)):]) == bomb) : 
      del stack[-(len(bomb)):]

      
if len(stack) == 0 : 
  print("FRULA")
else : 
  print("".join(stack))
  
    
      


