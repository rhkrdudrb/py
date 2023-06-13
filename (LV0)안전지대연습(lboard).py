# https://school.programmers.co.kr/learn/courses/30/lessons/172928
def solution(board):
    answer = 0
    # 경계생성
    R = len(board)
    C = len(board[0])
    for r in range(R):
        print()
        for c in range(C):
            if board[r][c] == 1:
                for dr,dc in((-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)):
                    nr,nc = r+dr,c+dc
                    # if nr < R or nr == 0 or nc == 0 or nc < C:
                    if 0 <= nr < R and 0 <= nc < C:    
                        if board[nr][nc] != 1:
                            board[nr][nc] = 2

    for i in range(R):
        for j in range(C):
            if board[i][j] == 0:
                answer+=1
    return answer
print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]))
# 0, 0, 0, 0, 0
# 0, 0, 0, 0, 0
# 0, 0, 0, 0, 0
# 0, 0, 1, 0, 0
# 0, 0, 0, 0, 0