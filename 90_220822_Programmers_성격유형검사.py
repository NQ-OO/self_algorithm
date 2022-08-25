

def solution(survey, choices):
    answer = ''
    char_lst = ["RT", "CF", "JM", "AN"]
    survey_result = {}
    for survey_idx in range(len(survey)) : 
        print(survey_result)
        if choices[survey_idx] < 4 : 
            if survey[survey_idx][0] in survey_result :
                survey_result[survey[survey_idx][0]] += (4 - choices[survey_idx])
            else : 
                survey_result[survey[survey_idx][0]] = (4 - choices[survey_idx])
        elif 4 < choices[survey_idx] < 8: 
            if survey[survey_idx][1] in survey_result :
                survey_result[survey[survey_idx][1]] += (choices[survey_idx] - 4)
            else : 
                survey_result[survey[survey_idx][1]] = (choices[survey_idx] - 4)
    
    print(survey_result)
    
    for result_idx in range(4) : 
      if (char_lst[result_idx][0] in survey_result) and (char_lst[result_idx][1] in survey_result) : 
        if survey_result[char_lst[result_idx][0]] < survey_result[char_lst[result_idx][1]] : 
          answer += char_lst[result_idx][1]
        else : 
          answer += char_lst[result_idx][0]
      elif (char_lst[result_idx][1] in survey_result) : 
        answer += char_lst[result_idx][1]
      else : 
        answer += char_lst[result_idx][0]
    
    return answer
  
  
  
survey = ["TR", "RT", "TR"]	
choices = [7,1,3]	
print(solution(survey, choices))