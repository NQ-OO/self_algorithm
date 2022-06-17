import sys
from collections import deque
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]
visit_num = [0] * (n+1)
q = deque([x])
answer = []

for __ in range(m) : 
  input_lst = list(map(int, input().split()))
  graph[input_lst[0]].append(input_lst[1])
  # graph[input_lst[1]].append(input_lst[0])


def bfs() :
  cnt = 1 
  visit_num[x] = 1
  while q : 
    now = q.popleft()
    cnt = visit_num[now] + 1
    for node in graph[now] : 
      if visit_num[node] == 0 : 
        visit_num[node] = cnt
        q.append(node)
        

bfs()

# print(answer)
for idx in range(1, n+1) :
  if visit_num[idx] == (k+1) : 
    answer.append(idx)

# print(graph)
# print(visit_num)

if len(answer) > 0 : 
  for node in answer :
    print(node)
else : 
  print(-1)