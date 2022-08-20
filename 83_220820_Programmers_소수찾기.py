

def solution(n):
    answer = 0
    prime_lst = []
    visited = [True] * (n+1)
    for idx in range(2, n+1) :
      print("idx :", idx)
      if visited[idx] : 
        prime_lst.append(idx)
        for m_idx in range(1, (n//idx)+1) : 
          print(n//idx)
          print("m_idx :",m_idx)
          visited[idx*m_idx] = False
    print(prime_lst)
    return len(prime_lst)  