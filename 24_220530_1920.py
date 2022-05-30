import sys
input = sys.stdin.readline

input_a_cnt = int(input())
input_a_lst = sorted(list(map(int, input().split())))
input_b_cnt = int(input())
input_b_lst = list(map(int, input().split()))

def binary_search(to_find) : 
  l = 0
  r = input_a_cnt-1
  
  while True : 
    m = (l + r)//2
    if to_find == input_a_lst[m] : 
      print(1)
      return
    elif l >= r : 
      print(0)
      return      
    elif to_find > input_a_lst[m] : 
      l = m + 1
    else : 
      r = m - 1
  
for to_find in input_b_lst :
  binary_search(to_find)
    
       
    



    
    
  
  