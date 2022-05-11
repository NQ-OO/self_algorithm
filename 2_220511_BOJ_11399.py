#18m 

num_cnt = int(input())
time_lst = sorted(list(map(int, input().split())))
sum_total_time = time_lst[0]
sum_lst = [time_lst[0]]

for time_idx in range(1, num_cnt) :
  sum_lst.append(sum_lst[time_idx-1] + time_lst[time_idx])
  sum_total_time += sum_lst[time_idx]

print(sum_total_time)


  

