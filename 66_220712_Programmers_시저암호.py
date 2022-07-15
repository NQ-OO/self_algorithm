def solution(s, n):
    answer = []
    for idx in range(len(s)) :
        if s[idx].isupper() : 
            answer.append(chr((ord(s[idx])-ord('A')+ n)%26 + ord('A')))
        elif s[idx].islower():
            answer.append(chr((ord(s[idx])-ord('a')+ n)%26+ord('a')))
        else : 
          answer.append(s[idx])
    return "".join(answer)

print(solution("AB", 1))