def solution(id_list, report, k):
    answer = [0]*len(id_list) 
    report_board = {string:[] for string in id_list}
    report_cnt = {string:0 for string in id_list}
    while report : 
      new = report.pop().split()
      if new[1] not in report_board[new[0]] : 
        report_cnt[new[1]] += 1 
        report_board[new[0]].append(new[1])
    for id_idx in range(len(id_list)) : 
      for user in report_board[id_list[id_idx]] : 
        if report_cnt[user] >= k : 
          answer[id_idx] += 1
    # print(report_board)
    return answer

id_list = ["muzi", "frodo", "apeach", "neo"]	
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]

# id_list = ["con", "ryan"]
# report = ["ryan con", "ryan con", "ryan con", "ryan con"]

print(solution(id_list, report, 2))



    # for id_idx in range(len(id_list)) : 
    #     for report_idx in range(len(report)) : 
    #         print(report[report_idx].split()[0])
    #         if id_list[id_idx] == report[report_idx][0] : 
    #             print(1)
    #             report_board[id_idx].append(report[report_idx][0])
    #             report_cnt[id_list[id_idx]] += 1