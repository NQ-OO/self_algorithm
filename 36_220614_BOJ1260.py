import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, (input().split()))
graph = [[] for _ in range(n+1)]
visited_dfs = [False] * (n+1)
visited_bfs = [False] * (n+1)


for _ in range(m) : 
  input_lst = list(map(int, input().split()))
  graph[input_lst[0]].append(input_lst[1])
  graph[input_lst[1]].append(input_lst[0])

for i in range(n+1) :
  graph[i] = sorted(graph[i])

def dfs(graph, v, visited) : 
  visited[v] = True
  print(v, end=" ")
  for idx in graph[v] :
    if not visited[idx] : 
      dfs(graph, idx, visited)

def bfs(graph, start, visited) : 
  q = deque([start])
  visited[start] = True
  while q : 
    v = q.popleft()
    print(v, end=" ")
    for node in graph[v] :
      if not visited[node] :
        q.append(node)
        visited[node] = True
    
dfs(graph, v, visited_dfs)
print()
bfs(graph, v, visited_bfs)
