


import sys
from collections import deque
from unittest import result
input = sys.stdin.readline

n, m = list(map(int, input().split()))
indegree = [0]*(n + 1)
graph = [[] for _ in range(n+1)]
q = deque()
result = []

for i in range(m) :
  input_num = list(map(int, input().split()))
  graph[input_num[0]].append(input_num[1])
  indegree[input_num[1]] += 1


for i in range(1, n+1) : 
  if indegree[i] == 0 : 
    q.append(i)


while len(q) != 0 : 
  now = q.popleft()
  result.append(now)
  for idx in graph[now] : 
    indegree[idx] -= 1
    if indegree[idx] == 0:
      q.append(idx)

for to_print in result :
  print(to_print, end=" ")
  


  




  
