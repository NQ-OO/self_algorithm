


from collections import deque
def solution(n, lost, reserve):
    answer = 0
    cnt = n - len(lost)
    lost.sort()
    reserve = reserve.sort()
    reserve_q = deque(reserve)
    
    while reserve : 
        now = reserve.pop()
        if now in lost : 
            lost.remove(now)
            cnt += 1
        elif (now + 1) in lost : 
            lost.remove(now + 1)
            cnt += 1
        elif (now - 1) in lost : 
            lost.remove(now - 1)
            cnt += 1
    answer = cnt

    return answer
  
print(solution(5, [2,4], [1,3,5]))