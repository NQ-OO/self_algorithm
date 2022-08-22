def solution(nums):
    answer = 0
    permutation_lst = [0]*3
    cnt = 0
    answer_lst = []
    
    def dfs(L, begin_with) : 
        if L == 3 :
            if is_prime(sum(permutation_lst)) : 
                answer_lst.append(1)
        else : 
            for idx in range(begin_with, len(nums)) : 
                permutation_lst[L] = nums[idx]
                dfs(L+1, idx + 1)
        return
    def is_prime(n) :
        prime_lst = [2, 3, 5, 7, 11, 13, 17, 19, 23]
        if n in prime_lst : 
            return(True)
        else : 
            return(False)
    dfs(0, 0)
    answer = len(answer_lst)
    
    return answer