

def reverse(str, new_str, cnt) : 
  if cnt == 0 : 
    return "".join(new_str)
  else : 
    new_str.append(str.pop())
    print(new_str)
    return reverse(str, new_str, cnt-1)

    
input_str = list(input())
str_len  = len(input_str) 

print(reverse(input_str,[], str_len))