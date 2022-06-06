#순서가 상관 없는 조합(combination)

num_lst = [1,2,3,4]
max_L = 3
answer = [0]*max_L

def DFS(L, start_with) : 
  if L == max_L : 
    print(answer)
  else : 
    for i in range(start_with, len(num_lst)) : 
      answer[L] = num_lst[i]
      DFS(L+1, i+1)

DFS(0, 0)