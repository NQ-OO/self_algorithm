


def factorial(input_num, result) : 
  if input_num == 0 :
    return result
  else : 
    return factorial(input_num-1, result*input_num)


print(factorial(int(input()), 1))


