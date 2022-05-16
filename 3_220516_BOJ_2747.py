

answer_lst = [0 for _ in range(50)]

input_num = int(input())

for idx in range(input_num+1) : 
  if idx == 0 : 
    answer_lst[0] = 0
  elif idx == 1 : 
    answer_lst[1] = 1
  else : 
    answer_lst[idx] = answer_lst[idx-1] + answer_lst[idx-2]
    

print(answer_lst[input_num])
