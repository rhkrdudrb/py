# https://school.programmers.co.kr/learn/courses/30/lessons/169199

def solution(board):
    R = len(board)
    C = len(board[0])                
    r, c = find_start(board)
    up = (r-1,c)
    # up: r,c -> 
    for r in range(R):
        for c in range(C):
            if board[r][c] == 'R':
                for dr,dc in[(-1, 0),(1,0),(0,-1),(0,1)]:
                    nr= r + dr # nr, nc는 이웃점들의 실제 좌표
                    nc= c + dc
                    if 0 <= nr < R and 0 <= nc < C:
                        print(1)
                        if board[nr][nc] == '.':
                            print(nr,nc)
    for i in range(R):
        print()
        for j in range(C):
            print(board[i][j] ,end='')

    return print("sssssssssssssssss")
def find_start(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'R':
                return i,j
# ...D..R
# .D.G...
# ....D.D
# D....D.
# ..D....
print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))
# ["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]	7
# [".D.R", "....", ".G..", "...D"]	-1

"...D..."
".D.G.R."
"....D.D"
"D....D."
"..D...."

# R: (1, 6) -> (0, 6)
# R: (1, 5) -> (0, 5)
# (r, c) -> (r-1, c)

# https://school.programmers.co.kr/learn/courses/30/lessons/172928
# def solution(park, routes):
#     # board = cr_board
#     board = cr_board(park)  #보드 생성
#     R = len(board)
#     C = len(board[0])
#     for i in range(R):
#         for j in range(C):
#             if board[i][j] == 'S':
#                 r,c = i,j
#     move = {"E":(0,1),"W":(0,-1),"S":(1,0),"N":(-1,0)} #동서남북 딕셔너리
#     for route in routes:
#         ewsn,boardmove = route.split()
#         dr,dc = move[ewsn]
#         nr,nc = r,c
#         for _ in range(int(boardmove)):
#             nr,nc = nr + dr, nc + dc
#             if nr < 0 or nr == R or nc < 0 or nc == C or board[nr][nc] =='X':
#                 nr,nc = r,c
#                 break
#         r, c = nr, nc
#     return nr,nc
# def cr_board(park):
#     board = []
#     for s in park:
#         s= list(s)
#         board.append(s)
#     return board    
# print(solution(["SOO","OOO","OOO"],["E 2","S 2","W 1"]))
# N : 북쪽으로 주어진 칸만큼 이동합니다.
# S : 남쪽으로 주어진 칸만큼 이동합니다.
# W : 서쪽으로 주어진 칸만큼 이동합니다.
# E : 동쪽으로 주어진 칸만큼 이동합니다.
# EWSN