
def dfs(L) : 
  if L == m : 
    for i in answer : 
      print(i, end=" ")
    print()
  else : 
    for idx in range(1, (n+1)) : 
      if not visited[idx] : 
        answer[L] = idx
        visited[idx] = True
        dfs(L+1)
        visited[idx] = False
        


n, m = map(int, input().split())
answer = [0]*m
visited = [False] * (n+1)

dfs(0)




