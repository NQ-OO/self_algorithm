input_num = int(input())

dp_table = [0] * 100
dp_table[1] = 1

def dp(n) : 
  if n == input_num + 1 : 
    print(dp_table[n-1])
  else : 
    dp_table[n] = dp_table[n-1] + dp_table[n-2]
    dp(n+1)
    

if input_num < 2 : 
  print(dp_table[input_num])
else : 
  dp(2)
# print(dp_table)