
input_str_lst_1 = list(input())
input_str_lst_2 = list(input())

dp_table = [[0] * (len(input_str_lst_2) + 1) for _ in range(len(input_str_lst_1) + 1)]

for row in range(1, len(input_str_lst_1)+1) :
  for col in range(1, len(input_str_lst_2)+1) : 
    if input_str_lst_1[row-1] == input_str_lst_2[col-1] : 
      dp_table[row][col] = dp_table[row-1][col-1] + 1
    else : 
        dp_table[row][col] = max(dp_table[row-1][col], dp_table[row][col-1])

print(dp_table[len(input_str_lst_1)][len(input_str_lst_2)])
      
      