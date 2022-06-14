#틀린 풀이 -> 문제점 : 문제를 정확하기 이해하지 못함. 
import sys
input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n+1)]
root_ready = [0] * (n+1)
root_ready[1] = 1
answer = [0] * (n+1)


for i in range(n-1) : 
  a, b = map(int, input().split())
  if root_ready[a] != 0 : 
    graph[a].append(b)
    root_ready[b] += 1
  else : 
    graph[b].append(a)
    root_ready[b] += 1

for idx in range(1, n+1) : 
  for node in graph[idx] : 
    answer[node] = idx

print(graph)
print(answer)

for answer_idx in range(2, n+1) :
  print(answer[answer_idx])
