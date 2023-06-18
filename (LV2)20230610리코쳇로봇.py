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
    check_list= [(r,c)]
    queue = deque([(0, r, c)])
    # dist = [[987654321 for _ in range(C)] for _ in range(R)] 
    while queue:
        n, r, c = queue.popleft() # 0,0,6
        if board[r][c]=='G':
                    return n 
        for dr,dc in [(-1,0),(1,0),(0,1),(0,-1)]: # (0,-1) #상,하,우,좌
            check = False
            nr,nc = r ,c #(0,5)
            while 0 <= nr+dr <  R and 0 <= nc+dc < C and board[nr+dr][nc+dc] != 'D': #안나가면
                nr  += dr
                nc  += dc
                check = True
                # if c - nc == 1: #왼쪽 dr,dc = (0,-1)
                # if c - nc == -1: #오른쪽 dr,dc = (0,1)
                #     r,c = r + dr ,c+dc 
                # if r - nr == 1: #위쪽 dr,dc = (-1,0)
                #     r,c = r+dr,c + dc
                # if r - nr == -1: #아래쪽 dr,dc = (1,0)
                #     r,c = r+dr,c + dc   
            if check:
                if (nr,nc) not in check_list:
                    queue.append((n + 1, nr, nc)) #(1,1,6)   
                    check_list.append((nr,nc))
                    print(queue)
    return -1
def start_point(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'R':
                return i,j
# print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))
print(solution([".D.R", "....", ".G..", "...D"]))
#------------------------------테스트 print 있음 ---------------------------------------
# def solution(board):
#     # nr,nc 움직인후 r+dr,c+dc
#     # dr,dr 움직일 좌표
#     # r,c 시작점
#     answer = 0
#     R = len(board)
#     C = len(board[0])
#     r,c = start_point(board)
#     check_list= [(r,c)]
#     queue = deque([(0, r, c)])
#     # dist = [[987654321 for _ in range(C)] for _ in range(R)]
#     while queue:
#         print('팝전 -> ', queue)
#         n, r, c = queue.popleft() # 0,0,6
#         print('팝후 -> ', queue)
#         print('시작점 -> ', r,c)
#         print('-------------------------------')
#         if board[r][c]=='G':
#                     return n 
#         for dr,dc in [(-1,0),(1,0),(0,1),(0,-1)]: # (0,-1) #상,하,우,좌
#             check = False
#             nr,nc = r ,c #(0,5)
#             while 0 <= nr+dr <  R and 0 <= nc+dc < C and board[nr+dr][nc+dc] != 'D': #안나가면
#                 nr  += dr
#                 nc  += dc
#                 check = True
#                 # if c - nc == 1: #왼쪽 dr,dc = (0,-1)
#                 # if c - nc == -1: #오른쪽 dr,dc = (0,1)
#                 #     r,c = r + dr ,c+dc 
#                 # if r - nr == 1: #위쪽 dr,dc = (-1,0)
#                 #     r,c = r+dr,c + dc
#                 # if r - nr == -1: #아래쪽 dr,dc = (1,0)
#                 #     r,c = r+dr,c + dc   
#             if check:
#                 # if dist[nr][nc] > c+1:
#                     # dist[nr][nc] = c+1
#                 print((nr,nc))
#                 print(check_list)
#                 print('----------')
#                 if (nr,nc) not in check_list:
#                     queue.append((n + 1, nr, nc)) #(1,1,6)   
#                     check_list.append((nr,nc))
#                     print(queue)
#     return -1
# def start_point(board):
#     for i in range(len(board)):
#         for j in range(len(board[i])):
#             if board[i][j] == 'R':
#                 return i,j
# # print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))
# print(solution([".D.R", "....", ".G..", "...D"]))
