
input_num = int(input())

frame = [[[] for _ in range(1 + (input_num-1)*4)] for _ in range(1 + (input_num-1)*4)]

# for idx in range(1 + (input_num-1)*4) : 
#   print(frame[idx])
  
def recur(input_num, idx) : 
  if (input_num-idx) == 0 : 
    return
  else : 
    start_point = frame[input_num//2+1 - (2 * idx)][input_num//2+1 - (2 * idx)]
    for star_idx in range(1 + (idx-1)*4) : 
      frame[input_num//2+1 - (2 * idx)][input_num//2+1 - (2 * idx)].append("*")
      


recur(input_num, 0)
for idx in range(1 + (input_num-1)*4) : 
  print(frame[idx])