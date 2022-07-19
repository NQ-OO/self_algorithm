# link : https://school.programmers.co.kr/learn/courses/30/lessons/62048
def solution(w,h):
    answer = 1
    def GCD(a, b) :   
        if a % b == 0:
            return b
        elif b == 0:
            return a
        else:
            return GCD(b, a % b)

    new_gcd = GCD(w, h)
    cross_block_num = (w/new_gcd + h/new_gcd - 1) * new_gcd
    answer = w * h - cross_block_num
    return answer    
  
  
  # def GDB(a, b) : 
  #   while b != 0 : 
  #     a, b = b, a % b
  #     return a 

      