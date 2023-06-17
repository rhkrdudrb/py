from collections import deque
# https://school.programmers.co.kr/learn/courses/30/lessons/169199

# 숙제: https://school.programmers.co.kr/learn/courses/30/lessons/154540
def solution(board):
    # nr,nc 움직인후 r+dr,c+dc
    # dr,dr 움직일 좌표
    # r,c 시작점
    answer = 0
    R = len(board)
    C = len(board[0])
    r,c = start_point(board)
    queue = deque([(0, r, c)])
    while queue:
        n, r, c = queue.popleft() # 0,0,6
        # for dr,dc in [(1,0),(-1,0),(0,-1),(0,1)]: # (0,-1)
        for dr,dc in [(1,0),(-1,0),(0,-1),(0,1)]: # (0,-1)
            check = False
            nr,nc = dr+r,dc+c #(0,5)
            while 0 <= nr <  R and 0 <= nc < C and board[nr][nc] != 'D': #안나가면
                # nr,nc = r + dr,c + dc
                r,c = r + dr,c + dc
                check = True
                break
                # if c - nc == 1: #왼쪽 dr,dc = (0,-1)
                # if c - nc == -1: #오른쪽 dr,dc = (0,1)
                #     r,c = r + dr ,c+dc 
                # if r - nr == 1: #위쪽 dr,dc = (-1,0)
                #     r,c = r+dr,c + dc
                # if r - nr == -1: #아래쪽 dr,dc = (1,0)
                #     r,c = r+dr,c + dc   
            if check:
                queue.append((n + 1, r, c)) #(1,1,6)
                print(queue)
                if board[r][c]=='G':
                    return n + 1
        break
    return -1
def start_point(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'R':
                return i,j

# lst = [1,2,3,4,5]
# lst.pop(0) # O(n)
# queue = deque([(1, 상), (2, 좌), (2, 하, (3, ))])

# ...D..R
# .D.G...
# ....D.D
# D....D.
# ..D....

# queue = [(1,1,6),(2,0,6),(2,1,4)]
# 1,0,4
# bfs: breadth first search

print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))
# ["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]	7
# [".D.R", "....", ".G..", "...D"]	-1
# https://school.programmers.co.kr/learn/courses/30/lessons/154540
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