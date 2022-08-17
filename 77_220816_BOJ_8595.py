import re

input_num = input()
input_str = input()
sum = 0
num_lst = re.split("[a-zA-Z]", input_str)
for num in num_lst : 
  if len(num) != 0 :
    sum += int(num)

print(sum)
