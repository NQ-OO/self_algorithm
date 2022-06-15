import queue
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
q = [[0, 0]]

for i in range(n): 
  graph.append(list(input()))
  graph[i].pop()
  
p_n = [-1, 1, 0, 0]
p_m = [0, 0, -1, 1]
  
def bfs(n, m) : 
  while q :
    now = q[0]
    del q[0]
    for idx in range(4) :
      next_step= [now[0]+p_n[idx], now[1]+p_m[idx]]
      if (0<= next_step[0] <n) and (0<= next_step[1] <m) :
        if graph[next_step[0]][next_step[1]] == "1" : 
          q.append(next_step)
          
          graph[next_step[0]][next_step[1]] = int(graph[now[0]][now[1]]) + 1
  return(graph[n-1][m-1])
          
print(bfs(n, m))
