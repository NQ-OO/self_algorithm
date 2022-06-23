
t = int(input())

for _ in range(t) : 
  n = int(input())
  coin_lst = list(map(int, input().split()))
  m = int(input())
  
  dp_table = [0] * (m + 2)
  dp_table[0] = 1
  
  for coin in coin_lst :
    for idx in range(coin, m+1) : 
      # if idx%coin == 0 : 
      dp_table[idx] = dp_table[idx - coin] + dp_table[idx]
  print(dp_table[m])
      

  
  