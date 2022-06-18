import sys
import heapq
from collections import deque


input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[]for _ in range(n+1)]
indegree = [0] * (n+1)
start_list = []
wait_q = deque()
answer = []

for idx in range(m) :
  input_lst = list(map(int, input().split()))
  graph[input_lst[0]].append(input_lst[1])
  indegree[input_lst[1]] += 1
  
for i in range(1, n+1) : 
  if indegree[i] == 0 : 
    heapq.heappush(start_list, i)
        
while start_list : 
  now = heapq.heappop(start_list)
  answer.append(now)
  for question in graph[now] :
    indegree[question] -= 1
    if indegree[question] == 0 :
      heapq.heappush(start_list, question)
    
    
for num in answer :
  print(num, end=" ")
  
  
