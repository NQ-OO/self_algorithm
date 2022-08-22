

def DFS(L) :
  if (L == N) : 
    answer = map(str, result)
    print(" ".join(answer))
  else : 
    for i in range(N) : 
      if checklist[i] == 0 : 
        result[L] = num_lst[i]
        checklist[i] = 1
        DFS(L + 1)
        checklist[i] = 0
    
    
N = int(input())
num_lst = list(range(1, N+1))

result = [0]*N
checklist = [0]*(N+1)

DFS(0)


