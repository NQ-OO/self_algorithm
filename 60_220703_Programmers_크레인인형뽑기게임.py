# https://programmers.co.kr/learn/courses/30/lessons/64061
def solution(board, moves):
    answer = 0
    stack = [0]
    for move_idx in range(len(moves)) : 
        for depth in range(len(board)) :
            new_value = board [depth][moves[move_idx]-1]
            if new_value != 0 : 
                board [depth][moves[move_idx]-1] = 0
                if stack[-1] == new_value: 
                    stack.pop()
                    answer +=2
                else : 
                    stack.append(new_value)
                break
            else : 
                pass
    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

print("sol :", solution(board, moves))