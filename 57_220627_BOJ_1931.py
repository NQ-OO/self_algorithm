import sys
from collections import deque
input = sys.stdin.readline

input_cnt = int(input())
input_lst = [ list(map(int, input().split())) for _ in range(input_cnt)]
visited_lst = []
input_len = len(input_lst)
last_cnt = 0

input_lst.sort(key=lambda x:x[1])
now = input_lst.pop(0)
visited_lst.append(now)
for _ in range(input_len) : 
  for time_int in range(len(input_lst)) : 
    if input_lst[time_int][0] >= visited_lst[-1][1] : 
      now = input_lst.pop(time_int)
      visited_lst.append(now)
      break

print(len(visited_lst))