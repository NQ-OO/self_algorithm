

def solution(nums):
    answer = 0
    prime_numbs = []
    
    def DFS(L, begin_with) :
      if L == r : 
        prime_numbs.append(sum(result))
      else : 
        for i in range(begin_with, len(n)) : 
            result[L] = n[i]
            DFS(L+1, i+1)
            
    def isPrime(n) : 
      answer = 0
      prime_lst = []
      visited = [True] * (n+1)
      for idx in range(2, n+1) :
        if visited[idx] : 
          prime_lst.append(idx)
          for m_idx in range(1, (n//idx)+1) : 
            visited[idx*m_idx] = False
      return (n in prime_lst)
      
    n = nums
    r = 3
    result = [0]*r
    DFS(0, 0)
    prime_numbs_lst = list(prime_numbs)
    
    for idx in prime_numbs_lst :
      if isPrime(idx) : 
        answer += 1

    return answer

print(solution([1,2,7,6,4]))