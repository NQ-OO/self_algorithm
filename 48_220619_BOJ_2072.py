#3:00
import sys
from collections import deque
input = sys.stdin.readline

board = [[0] * 21 for _ in range(21)]
round_cnt = int(input())
total_lst = []
y_lst = []
x_lst = []

def find_start_point(y_lst, x_lst) : 
  start_point_lst = []
  check_if_not_first_d_y = [0, -1, -1, -1]
  check_if_not_first_d_x = [-1, -1, 0, 1]
  check_if_first_d_y = [0, 1, 1, 1]
  check_if_first_d_x = [1, 1, 0, -1]
  
  for i in range(len(y_lst)):
    y = y_lst[i]
    x = x_lst[i]
    now = board[y][x]
    if (now == 1) or (now == -1) :
      for i in range(4) : 
        if board[y + check_if_first_d_y[i]][x + check_if_first_d_x[i]] == now : 
          if board[y + check_if_not_first_d_y[i]][x + check_if_not_first_d_x[i]] != now : 
            start_point_lst.append([y, x, i])
  
  return(start_point_lst)
              
            
            
def check_five(start_point_lst) : 
  d_y = [0, 1, 1, 1]
  d_x = [1, 1, 0, -1]
  cnt_lst = []
  
  for start_point in start_point_lst : 
    now = board[start_point[0]][start_point[1]]
    cnt = 0
    while True : 
      if now  == board[start_point[0]+(d_y[start_point[2]]*(cnt+1))][start_point[1]+(d_x[start_point[2]]*(cnt+1))] : 
        cnt += 1
      else : 
        cnt_lst.append(cnt)
        break
  if 4 in cnt_lst : 
    return True
        


for idx in range(round_cnt) :
  total_lst.append(list(map(int, input().split())))
  
for idx in range(len(total_lst)) : 
  y, x = total_lst[idx]
  y_lst.append(y)
  x_lst.append(x)
  point_lst = []
  if idx%2 == 1 : 
    board[y][x] = -1
  else : 
    board[y][x] = 1
  if idx > 7 : 
    # print("idx1 :", idx)
    start_point_lst = find_start_point(y_lst, x_lst)
    if check_five(start_point_lst) : 
      print(idx+1)
      break
  if idx == round_cnt-1 : 
    print(-1)
    

# for row in board :
#   print(row)