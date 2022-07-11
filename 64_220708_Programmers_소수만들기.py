def solution(nums):
    answer = -1
    permutation_lst = [0]*3
    cnt = 0
    
    def dfs(L, begin_with, cnt) : 
        if L == 3 :
            if is_prime(sum(permutation_lst)) : 
                cnt += 1
                print("cnt :", cnt)
        else : 
            for idx in range(begin_with, len(nums)) : 
                permutation_lst[L] = nums[idx]
                dfs(L+1, idx + 1)
        return cnt
    def is_prime(n) :
        prime_lst = [2, 3, 5, 7, 11, 13, 17, 19, 23]
        if n in prime_lst : 
            return(True)
        else : 
            return(False)
    print(dfs(0, 0))
    print(cnt)
    
        
    return answer

solution([1,2,7,6,4])