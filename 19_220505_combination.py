#rCn


def DFS(L, begin_with) : 
  if L == r : 
    print(answer)
  else : 
    for i in range(begin_with, len(n)) : 
      answer[L] = n[i]
      DFS(L+1, i+1)
  

n = [1,2,3,4,5]
r = 3

answer = [0] * r

DFS(0, 0)