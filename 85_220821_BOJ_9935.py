

import sys
input = sys.stdin.readline

input_str = list(input().strip())
bomb = list(input().strip())
stack = []


for comparing_char in input_str : 
  stack.append(comparing_char)
  if (len(stack) >= len(bomb)) and (stack[-1] == bomb[-1]) : 
    if "".join(stack[-(len(bomb)):]) == "".join(bomb) : 
      for _ in range(len(bomb)) : 
        stack.pop()

result = "".join(stack)
if len(result) > 0 : 
  print(result)
else : 
  print("FRULA")
      
  
  
