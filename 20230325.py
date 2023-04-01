# https://school.programmers.co.kr/learn/courses/30/lessons/172928?language=python3
def solution(park, routes):
    board = create_board(park)         
    return move_if_possible(routes, board)

def create_board(park):
    board =[]
    for s in park: # SOO, 
        s = list(s)
        board.append(s)
    return board
    
def create_board_start(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'S':
                return i, j

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

s = "abcd"
for letter in s:
    print(letter)

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
