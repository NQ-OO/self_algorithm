def solution(n, m):
    answer = []
    num_lst = sorted([n, m])
    left = num_lst[1] % num_lst[0]
    while n : 
        tmp = m % n;
        m = n;
        n = tmp;
    gcd = m
    print(gcd)
    lcd = (num_lst[0]//gcd) * num_lst[1]
    answer = [gcd, lcd]
        
    return answer
  