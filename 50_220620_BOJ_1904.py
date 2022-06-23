
input_num = int(input())
dp = [0] * (input_num + 2)
dp[1] = 1
dp[2] = 2

if input_num > 2 : 
  for idx in range(3, input_num+1) : 
    dp[idx] = (dp[idx-1] + dp[idx-2])%15746
  
print(dp[input_num])
  
