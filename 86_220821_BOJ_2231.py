

input_num = int(input())

answer = 0
for create_sum in range(1, input_num) :
  sum_num = create_sum
  seperate_num_lst = list(map(int, str(create_sum)))
  sum_num += sum(seperate_num_lst)
  if sum_num == input_num : 
    answer = create_sum
    break

print(answer)

  



