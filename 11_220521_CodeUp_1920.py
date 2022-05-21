

input_num = int(input())
binary_lst = []

def binary(int) : 
  if int == 0 :
    if len(binary_lst) > 0 : 
      return binary_lst
    else : 
      binary_lst.append(str(0))
      return binary_lst
    
  left_over = int%2
  binary_lst.append(str(left_over))
  return binary(int//2)
  
  
binary_value_lst = binary(input_num)
print("".join(binary_value_lst[::-1]))
