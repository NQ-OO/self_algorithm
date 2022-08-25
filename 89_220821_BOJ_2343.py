
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
input_lst = list(map(int, input().split()))
input_len = len(input_lst)
sum_input = sum(input_lst)
l = sum_input//(M-1)
r = sum_input//(M+1)

def isPossible(max_hop, M) : 
  hop_cnt = 0
  cnt = 0
  sum = 0
  sum_lst = []
  while sum <= max_hop : 
    sum += input_lst[input_len - cnt]
    cnt += 1
    
  

  print("cnt :", cnt)
  if cnt > M : 
    return False
  else : 
    return True 
      


while r > l : 
  c = (l+r)//2


print(sum_input)
 

print(isPossible(17, M))