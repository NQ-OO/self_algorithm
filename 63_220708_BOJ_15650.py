
def dfs(L, begin_with) : 
  if L == m : 
    for i in answer : 
      print(i, end=" ")
    print()
  else : 
    for idx in  range(begin_with, n+1) : 
      answer[L] = idx
      dfs(L + 1, idx + 1)
  
  
  
n, m  = map(int, input().split())
answer = [0] * m
dfs(0, 1)
