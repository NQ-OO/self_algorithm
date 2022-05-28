from copy import deepcopy


input_num = int(input())
answer = [0]*input_num
step_lst = [1,2,3]
answer_lst = []
cnt = 0

def recur(L) :
  if input_num == sum(answer) : 
    lst_to_append = deepcopy(answer)
    answer_lst.append(lst_to_append)
    
    return 
  elif sum(answer) > input_num : 
    return 
  else : 
    for idx in range(len(step_lst)) : 
      if input_num >=  sum(answer) + step_lst[idx] : 
        answer[L] = step_lst[idx]
        recur(L+1)
        answer[L] = 0
        

recur(0)
print(len(answer_lst))
      
      
