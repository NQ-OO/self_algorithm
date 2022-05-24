import sys
input = sys.stdin.readline
input_lst = []

    
def combination(L, begin_with) :
  if L == 6 : 
    print(" ".join(answer))
  else : 
    for i in range(begin_with, len(single_input)-1) : 
      # print(answer)
      answer[L] = single_input[i+1]
      combination(L+1, i+1)
    
while True : 
  single_input = input().split()
  if int(single_input[0]) == 0 :
    break
  answer = [0] * 6
  combination(0, 0)
  print()
  
  
  

  
  