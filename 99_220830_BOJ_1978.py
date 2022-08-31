input_cnt = input()
cnt = 0
li = list(map(int, input().split()))
for idx in li : 
  f = True
  if idx <= 1 : 
    continue
  for dividing_num in range(2, idx) : 
    if idx%dividing_num == 0 : 
      f = False
      break
  if f : 
    cnt += 1
print(cnt)

