# https://school.programmers.co.kr/learn/courses/30/lessons/172928
def solution(park, routes):
    board = cr_board(park)
    R = len(board)
    C = len(board[0])
    r,c =starting_point(board,R,C)
    print(r,c)
    move = {"E":(0,1),"W":(0,-1),"S":(1,0),"N":(-1,0)} #동서남북 딕셔너리
    for route in routes:
        eswn,onemove = route.split()
        dr,dc = move[eswn] #움직이는 좌표
        nr,nc = r,c
        for _ in range(int(onemove)):
            nr,nc = nr+dr,nc+dc
            if nr < 0 or nr == R or nc < 0 or nc == C or board[nr][nc] =='X':
                nr,nc = r,c
                break
        r,c = nr,nc
    return nr,nc
def cr_board(park):
    board = []
    for s in park:
        s =list(s)
        board.append(s)
    return board
def starting_point(board,R,C):
    for i in range(R):
        for j in range(C):
            if board[i][j] == 'S':
                 r,c = i,j
    return r,c

print(solution(["SOO","OOO","OOO"],["E 2","S 2","W 1"]))
print(solution(["SOO","OXX","OOO"],["E 2","S 2","W 1"]))
print(solution(["OSO","OOO","OXO","OOO"],["E 2","S 3","W 1"]))
# N : 북쪽으로 주어진 칸만큼 이동합니다.
# S : 남쪽으로 주어진 칸만큼 이동합니다.
# W : 서쪽으로 주어진 칸만큼 이동합니다.
# E : 동쪽으로 주어진 칸만큼 이동합니다.