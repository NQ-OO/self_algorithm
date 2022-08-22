
import sys
input = sys.stdin.readline

N = int(input())
N_lst = (set(map(int, input().split())))
# N_lst = list(set(map(int, input().split())))
M = int(input())
M_lst = list(map(int, input().split()))


def in_lst(idx, N) : 
  # l_idx = 0
  # r_idx = N-1
  if idx in N_lst : 
    return True
  else : 
    return False
    
  
  # while True :
  #   c_idx = (l_idx + r_idx)//2
  #   # print("-----------------------")
  #   # print(N_lst)
  #   # print("idx :", idx)
  #   # print("l :", N_lst[l_idx])
  #   # print("r :", N_lst[r_idx])
  #   # print("c :", N_lst[c_idx])
  #   if idx == N_lst[c_idx] : 
  #     return True
  #   elif N_lst[r_idx] <= N_lst[l_idx] : 
  #     return False
  #   elif idx > N_lst[c_idx] : 
  #     l_idx = c_idx + 1
  #   else : 
  #     r_idx = c_idx - 1
    


for idx in M_lst :
  if in_lst(idx, N) : 
    print(1, end=" ")
  else : 
    print(0, end=" ")