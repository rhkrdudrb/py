# https://school.programmers.co.kr/learn/courses/30/lessons/160585
def solution(board):
    o_cnt = 0
    x_cnt = 0
    answer = 1
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] =='O':
                o_cnt += 1
            if board[i][j] =='X':
                x_cnt += 1
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2]: #세로 같은때
            answer = 0
        if board[0][i] == board[1][i] and board[1][i] == board[2][i]: #가로 같을때
            answer = 0
    if board[0][0] == board[1][1] and board[0][0] == board[2][2]: #대각선(\) 같을때
        answer = 0
    if board[0][2] == board[1][1] and board[0][2] == board[2][0]: #대각선(/) 같을때
        answer = 0 
    if o_cnt < x_cnt: #실수할때(선공이 없는데 후공이 먼저할때)
        answer = 0
    if o_cnt == 0 and x_cnt == 0 : #선공 후공 아무도 공격하지 않을때
        return  1
    if o_cnt== 5 and x_cnt == 4 : #두줄 빙고시
        return 1
    if o_cnt== 4 and x_cnt == 5 : #두줄 빙고시
        return 1
    return answer
# o,x둘중 이기는 사람 판단해서 cnt가지고 판단하기
# o가 이기면 o = x+1
# x가 이기면 o = x
print(solution(["O.X", ".O.", "..X"]))
print(solution(["OOO", "...", "XXX"]))
print(solution(["...", ".X.", "..."]))
print(solution(["...", "...", "..."]))


