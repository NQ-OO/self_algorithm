
# 모든 수의 조합을 구한다

def DFS(L) : 
  if L == n : 
    print(result)
  else : 
    for i in range(len(r)) : 
      if check_lst[i] == 0 : 
        check_lst[i] = 1
        result[L] = r[i]
        DFS(L+1)
        check_lst[i] = 0

r = [1,2,3,4,5]
n = 3

check_lst = [0]*len(r)
result = [0]*n

DFS(0)




# def DFS(L, begin_with) : 
#   if L == n : 
#     print(result)
#   else : 
#     for i in range(begin_with, len(r)) : 
#       result[L] = r[i]
#       DFS(L+1, i+1)
    


# r = [1,2,3,4,5]
# n = 3

# result = [0]*n
# DFS(0,0)
