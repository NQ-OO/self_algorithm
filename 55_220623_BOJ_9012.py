input_num = int(input())
ps_lst = []
for _ in range(input_num) : 
  
  ps = list(input())
  cnt = 0 
  while len(ps) != 0 :  
    if ps.pop() == ')' :
      cnt += 1
    else : 
      cnt -= 1
      if cnt < 0 : 
        print('NO')
        break
    
  if cnt  == 0 : 
    print("YES")
  elif cnt > 0 : 
    print("NO")

      
      
  
  
  
