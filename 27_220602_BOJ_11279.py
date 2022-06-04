import sys
import heapq
input = sys.stdin.readline
heap_lst = []

input_cnt = int(input())

for _ in range(input_cnt) :
  new_input = int(input())
  if new_input == 0 : 
    if len(heap_lst) == 0 : 
      print(0)
    else : 
      print(-heapq.heappop(heap_lst))
  else : 
    heapq.heappush(heap_lst, -new_input)
  
      