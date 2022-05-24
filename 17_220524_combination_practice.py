
def DFS(L, begin_with) :
  if L == r : 
    print(result)
  else : 
    for i in range(begin_with, len(n)) : 
        result[L] = n[i]
        DFS(L+1, i+1)
  

n = [1,2,3,4,5]
r = 3

result = [0]*r

DFS(0, 0)