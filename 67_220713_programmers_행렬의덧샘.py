def solution(arr1, arr2):
    answer = []
    
    for idx_1 in range(len(arr1)) : 
        sub_answer = []
        for idx_2 in range(len(arr1[1])) : 
            sub_answer.append(arr1[idx_1][idx_2] + arr2[idx_1][idx_2])
        answer.append(sub_answer)
    return answer