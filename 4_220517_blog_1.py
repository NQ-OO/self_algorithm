

def cnt_num_reversed(num) : 
  if num == 0 : 
    print(0)
    return
  else : 
    print(num)
    return cnt_num_reversed(num-1)
    
cnt_num_reversed(int(input()))
