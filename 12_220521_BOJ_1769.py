
input_lst = list(str(input()))
cnt = 0

def make_add_up_int(input_lst, cnt) :
  input_int_joined = int("".join(input_lst))
  if input_int_joined < 10 : 
    if input_int_joined % 3 == 0 : 
      print(cnt)
      print("YES")
      return

    else : 
      print(cnt)
      print("NO")  
      return
  cnt += 1
  input_int = map(int, input_lst)
  sum_int = sum(input_int)
  return make_add_up_int(list(str(sum_int)), cnt)
  

make_add_up_int(input_lst, cnt)
  