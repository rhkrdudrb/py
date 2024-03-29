# https://school.programmers.co.kr/learn/courses/30/lessons/172928?language=python3
def solution(park, routes):
    board = create_board(park)         
    return move_if_possible(routes, board)
#보드 생성
def create_board(park):
    board =[]
    for s in park: # SOO, 
        s = list(s)
        board.append(s)
    return board
#보드 시작점     
def create_board_start(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'S':
                return i, j
#한칸씩이동하면서 보드 장애물 범위 체크
def move_if_possible(routes,board):
    r, c = create_board_start(board)
    R = len(board)
    C = len(board[0])
    move = {"E":(0,1),"W":(0,-1),"S":(1,0),"N":(-1,0)} #동서남북 딕셔너리
    for route in routes:
        ewsn,move = route.split()
        dr,dc = move[ewsn]
        new_r,new_c = r,c
        for _ in range(int(move)):
            new_r, new_c = new_r + dr, new_c + dc
            if new_r < 0 or new_r == R or new_c < 0 or new_c  == C or board[new_r][new_c] == "X":
                new_r,new_c = r,c
                break
        r, c = new_r, new_c
    return r,c

# [1,2,3] -> 2

s = "abcd"
for letter in s:
    print(letter)
#한칸씩 이동하면서 장애물 체크 및 보드 범위 체크
# S : 시작 지점
# O : 이동 가능한 통로
# X : 장애물
# op는 다음 네 가지중 하나로 이루어져 있습니다.
# N : 북쪽으로 주어진 칸만큼 이동합니다. []
# S : 남쪽으로 주어진 칸만큼 이동합니다. []
# W : 서쪽으로 주어진 칸만큼 이동합니다. []
# E : 동쪽으로 주어진 칸만큼 이동합니다. []
print(solution(["SOO","OOO","OOO"], ["E 2","S 2","W 1"]))
# park routes
# ["SOO","OOO","OOO"]	["E 2","S 2","W 1"]	[2,1]
# SOO
# OOO
# OOO
# ["SOO","OXX","OOO"]	["E 2","S 2","W 1"]	[0,1]
# SOO
# OXX
# OOO
# ["OSO","OOO","OXO","OOO"]	["E 2","S 3","W 1"]	[0,0]
# OSO
# OOO
# OXO
# OOO
# 20230616 복습
def solution(park, routes):
    #1.보드생성
    board = cr_board(park)
    #2.보드시작점
    r,c = start_point(board)
    #3.보드경계
    R = len(board)
    C = len(board[0])
    print(r,c)
    move = {"E":(0,1),"W":(0,-1),"S":(1,0),"N":(-1,0)} #동서남북 딕셔너리
    for route in routes:
        ewsn,one_move = route.split()
        dr,dc = move[ewsn]
        nr,nc = r,c
        for _ in range(int(one_move)):
            nr,nc = nr+dr , nc+dc
            if nr < 0 or nr == R or nc < 0 or nc == C or board[nr][nc] =='X':
                nr,nc = r,c
                break
        r,c = nr,nc
    return nr,nc
def cr_board(park):
    board = []
    for s in park:
        s = list(s)
        board.append(s)
    return board
def start_point(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "S":
                return i,j
