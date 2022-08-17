import sys
input = sys.stdin.readline

input_num_lst_cnt = input()
first_num_lst = input().split()
second_num_lst = input().split()

print(" ".join(map(str, sorted(first_num_lst + second_num_lst))))



################ 이게 맞는 답! 틀린 이유를 모르겠다 ###############
# import sys

# a, b = map(int, sys.stdin.readline().split())
# a_list = list(map(int, sys.stdin.readline().split()))
# b_list = list(map(int, sys.stdin.readline().split()))
# answer_list = a_list + b_list
# answer = ' '.join(map(str, sorted(answer_list)))
# print(answer)
