
input_num = int(input())

dividing_num = 2
while input_num != 1 : 
  if input_num % dividing_num == 0 : 
    input_num /= dividing_num
    print(dividing_num)
  else :
    dividing_num += 1
    