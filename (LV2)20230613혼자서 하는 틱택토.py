# https://school.programmers.co.kr/learn/courses/30/lessons/160585
def solution(board):
    #규칙을 지켜서 진행한 틱택토에서 나올 수 있는 상황인가 아닌가
    o_cnt,x_cnt = oxcnt(board)
    o_victory,x_victory = ox_check_victory(board)
    return possible_impossible(o_cnt,x_cnt,o_victory,x_victory)
def possible_impossible(o_cnt,x_cnt,o_victory,x_victory):
    if o_cnt < x_cnt: # 후공이 2번 둔 경우 (나올수 없는상황) 
        return 0
    if o_cnt > x_cnt+1: # 선공이 2번둔 경우 (나올수없는상황)
        return 0
    if o_cnt + x_cnt ==0: #선공후공 아무도 안둔경우 (나올수있는상황)
        return 1
    if o_victory ==0 and x_victory ==0: #아무도 못이긴경우 (나올수있는상황)
        return 1
    if 0 < o_victory and x_victory ==0 and o_cnt > x_cnt: # o이 이긴경우 한줄빙고 (나올수있는상황)!
        return 1
    if 0 < x_victory and o_victory ==0 and x_cnt == o_cnt: # x가 이긴경우 한줄빙고 (나올수있는상황)!
        return 1
    return 0 #(나머지 경우)
def oxcnt(board):
    o = 0
    x = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] =='O':
                o += 1
            if board[i][j] =='X':
                x += 1
    return o,x
def ox_check_victory(board):
    o_cnt = 0
    x_cnt = 0
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2]: #세로 같은때
            if board[i][1] == 'O':
                o_cnt += 1
            if board[i][1] == 'X':
                x_cnt += 1
        if board[0][i] == board[1][i] and board[1][i] == board[2][i]: #가로 같을때
            if board[1][i] == 'O':
                o_cnt += 1
            if board[1][i] == 'X':
                x_cnt += 1
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]: #대각선(\) 같을때
        if board[1][1] == 'O':
            o_cnt +=1
        if board[1][1] == 'X':
            x_cnt +=1
    if board[0][2] == board[1][1] and board[1][1] == board[2][0]: #대각선(/) 같을때
        if board[1][1] == 'O':
            o_cnt +=1
        if board[1][1] == 'X':
            x_cnt +=1
    return o_cnt,x_cnt
# o,x둘중 이기는 사람 판단해서 cnt가지고 판단하기
# o가 이기면 o = x+1
# x가 이기면 o = x
print(solution(["O.X", ".O.", "..X"]))
print(solution(["OOO", "...", "XXX"]))
print(solution(["...", ".X.", "..."]))
print(solution(["...", "...", "..."]))


