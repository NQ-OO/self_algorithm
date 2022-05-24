# rPn


def DFS(L) : 
  if L == r : 
    print(answer)
  else : 
    for i in range(len(n)) : 
      if visited[i] == 0 : 
        answer[L] = n[i]
        visited[i] = 1
        DFS(L+1)
        visited[i] = 0

n = [1,2,3,4,5,6]
r = 4
answer = [0]*4
visited = [0]*len(n)

DFS(0)