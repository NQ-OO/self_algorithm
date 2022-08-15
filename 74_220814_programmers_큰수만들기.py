
from heapq import heapify, heappop


def solution(number, k):
    answer = ''
    number_lst = list(number)
    number_heap = list(number)
    heapify(number_heap)
    
    while k > 0 : 
        for number_idx in range(1, len(number_lst)) : 
          if number_lst[number_idx-1] < number_lst[number_idx] : 
              number_lst.pop(number_idx-1)
              k -= 1
              break
        else : 
            min_num = heappop(number_lst)
            print(min_num)
            number_lst.pop(str(min_num))
            k -= 1
    answer = "".join(number_lst)
            
    return answer
  
  
print(solution("1000000", 4))