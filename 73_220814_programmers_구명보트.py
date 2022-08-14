#10:51


from collections import deque

def solution(people, limit):
    answer = 0
    sorted_people = deque(sorted(people))
    while len(sorted_people) != 0 : 
        first_person = sorted_people[0]
        last_person = sorted_people.pop()
        if (first_person + last_person) > limit : 
            answer += 1
        else : 
            if len(sorted_people) > 0 : 
              sorted_people.popleft()
            answer += 1
    return answer
  
  
print(solution([50, 70, 80], 100))