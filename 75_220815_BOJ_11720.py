import sys 
input = sys.stdin.readline

num_cnt = int(input())

input_num = input()
print(sum(map(int,list(input_num)[:-1])))