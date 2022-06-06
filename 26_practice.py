#순서가 상관 있는 순열을 만들어보자.

from itertools import permutations


input_cnt = 3
max_L = 3
visited = [0]*input_cnt
answer = [0]*3
input_num_lst = [1,2,3]

def DFS(L) : 
  if L == max_L : 
    print(answer)
    # return
  else : 
    for i in range(input_cnt) : 
      if visited[i] == 0 : 
        visited[i] = 1
        answer[L] = input_num_lst[i]
        DFS(L+1)
        visited[i] = 0
        
DFS(0)
        
        
  
  
  

  
  
  
  
  