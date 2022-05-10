import sys
input = sys.stdin.readline

n, m, k  = map(int, input().split())
num_lst = sorted(list(map(int, input().split())), reverse=True)

result = 0

for idx in range(1, m+1) : 
  if idx % (k+1) == 0 :
    result += num_lst[1]
  else : 
    result += num_lst[0]
    
print(result)
    
    