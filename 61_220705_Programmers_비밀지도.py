def solution(n, arr1, arr2):
    answer = []
    board = [[" " for _ in range(n)] for __ in range(n)]
    arr1_bin = [list(format(value, 'b').zfill(n)) for value in arr1]
    arr2_bin = [list(format(value, 'b').zfill(n)) for value in arr2]
    for i in range(n) :
        for j in range(n) :
            if (arr1_bin[i][j] == "1") or (arr2_bin[i][j] == "1"):
                board[i][j] = '#'
    answer = ["".join(row) for row in board]
    return answer