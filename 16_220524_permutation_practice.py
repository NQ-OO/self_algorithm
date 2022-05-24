#순열(permutation) : 순서가 상관 있음. 




def DFS(L) : 
  ## 종료조건 
  if (L == n) : 
    print(result)
  else : 
    for i in range(len(r)) :
      if checklist[i] == 0 :
        result[L] = r[i]
        checklist[i] = 1
        DFS(L+1)
        checklist[i] = 0
      
r = [1,2,3,4,5]
n = 3

result = [0]*n
checklist = [0]*len(r)

DFS(0)
