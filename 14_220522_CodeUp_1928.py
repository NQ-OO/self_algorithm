


input_num = int(input())


def recur(n) :
  print(n)
  if n == 1 :
    return
  elif n % 2 == 1 :
    n = 3*n + 1
    recur(n)
  else : 
    n = n//2
    recur(n)

recur(input_num)
    

  