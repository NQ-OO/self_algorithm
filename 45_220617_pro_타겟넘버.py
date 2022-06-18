



def solution(numbers, target):
    answer = 0
    signs = [1, -1]
    answer_lst = []
    sign_lst = [0]*len(numbers)
    
    def dfs(L, answer) : 
      if L == len(numbers) : 
        temp = 0
        for idx in range(len(numbers)) :
          temp += sign_lst[idx] * numbers[idx]
        if temp == target :
          answer_lst.append(answer)
          print(answer_lst)
      else : 
        for i in range(len(signs)) :
          sign_lst[L] = signs[i]
          dfs(L+1, answer)
    dfs(0 , answer)      
    answer = len(answer_lst)
    return answer
  
numbers = [1,1,1,1,1]
target = 3

print(solution(numbers, target))
