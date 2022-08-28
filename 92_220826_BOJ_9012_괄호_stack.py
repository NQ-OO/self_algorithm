import sys
input = sys.stdin.readline
input_cnt = int(input())


for i in range(input_cnt) : 
  stack= []
  ps = input().strip()
  for p in ps : 
    if p == '(' : 
      stack.append(p)
    elif stack : 
      stack.pop()
    else : 
      print("NO")
      break 
  else : 
    if stack : 
      print("NO")
    else :
      print("YES")


