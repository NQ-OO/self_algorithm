
plate_cnt = int(input())
cnt_lst = [0]*101
cnt_lst[0] = 1

def cnt_recur(n) : 
  for idx in range(1, n):
    cnt_lst[idx] = 2* cnt_lst[idx-1] + 1
  return cnt_lst[n-1]

    
def recur(plate_cnt, a, through, b) : 
  if plate_cnt == 1 : 
    print(a, b)
  else : 
    return recur(plate_cnt-1, a, b, through), recur(1, a, through, b), recur(plate_cnt-1,through, a, b) 
  
print(cnt_recur(plate_cnt))
if plate_cnt <= 20 : 
  recur(plate_cnt, 1, 2, 3)


