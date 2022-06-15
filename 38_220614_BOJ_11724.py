import sys
sys.setrecursionlimit(10**4)
input = sys.stdin.readline


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited_dfs = [False] * (n+1)
visited_lst = [False] * (n+1)
answer = 0


for __ in range(m) :
  u, v = map(int, input().split())
  graph[u].append(v)
  graph[v].append(u)


def dfs(graph, v, visited) : 
  visited[v] = True
  visited_lst[v] = True
  for node in graph[v] : 
    if not visited[node] : 
      dfs(graph, node, visited)


for idx in range(1, n+1) : 
  if not visited_lst[idx] :
    dfs(graph, idx, visited_dfs)
    answer +=1

print(answer)
    
    
