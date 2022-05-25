

input_num = int(input())

frame_len = input_num*4 - 3
frame = [[" " for __ in range(frame_len)] for _ in range(frame_len)]

def recur(n) : 
  if n == (frame_len//2 + 1) :
    frame[frame_len//2][frame_len//2] ="*"
  else : 
    start_point = 2*n
    side_len = (frame_len - n*4)
    for idx_num in range(start_point, start_point+ side_len) :
      frame[start_point][idx_num] = "*" ## top
      frame[start_point+side_len-1][idx_num] = "*" ##bottom
      frame[idx_num][start_point] = "*" ##left
      frame[idx_num][start_point + side_len-1] = "*" ##right
    recur(n+1)


recur(0)

for idx in range(1 + (input_num-1)*4) : 
  print("".join(frame[idx]))