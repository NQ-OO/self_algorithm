import sys
input = sys.stdin.readline

n, k = map(int, input().split())
stack = []
item_lst = []
board = [[0] * (k+1) for _ in range(n+1)]

for _ in range(n) : 
  new = list(map(int, input().split())) 
  item_lst.append(new)
  item_lst.sort(key = lambda x:x[0])

for n_idx in range(1, n+1) : 
  for k_idx in range(1, k+1) : 
    if k_idx - item_lst[n_idx-1][0] >= 0 : 
      board[n_idx][k_idx] = max(board[n_idx-1][k_idx], board[n_idx-1][k_idx - item_lst[n_idx-1][0]] + item_lst[n_idx-1][1])
    else : 
      board[n_idx][k_idx] = board[n_idx-1][k_idx] 

print(board[n][k])
      
      
  









