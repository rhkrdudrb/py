# https://school.programmers.co.kr/learn/courses/30/lessons/172928
def solution(park, routes):
    # 보드생성
    board = cr_board(park)
    # 보드경계
    R = len(board)
    C = len(board[0])
    # 시작점
    for i in range(R):
        for j in range(C):
            if board[i][j] == 'S':
                r,c = i,j
    move = {"N":(-1,0),"S":(1,0),"W":(0,-1),"E":(0,1)} #동서남북 한칸씩
    for route in routes:
        ewsn,onemove = route.split()
        dr,dc = move[ewsn] # dr,dc 움직이는 방향 꼭 외우기 !!!
        nr,nc = r,c        # 시작 위치
        for _ in range(int(onemove)):
            nr,nc = nr+dr,nc+dc # 시작좌표 + 움직인 좌표(이동한 좌표)
            if nr < 0 or nr == R or nc < 0 or nc == C or board[nr][nc] == 'X':
                nr,nc = r,c # 시작위치로 초기화
                break
        r,c =nr,nc #이동가능한 좌표 저장
        print(r,c)
    return nr,nc
def cr_board(park):
    board = []
    for s in park:
        s = list(s)
        board.append(s)
    return board
print(solution(["SOO","OOO","OOO"],["E 2","S 2","W 1"]))
print(solution(["SOO","OXX","OOO"],["E 2","S 2","W 1"]))
print(solution(["OSO","OOO","OXO","OOO"],["E 2","S 3","W 1"]))
# N : 북쪽으로 주어진 칸만큼 이동합니다.
# S : 남쪽으로 주어진 칸만큼 이동합니다.
# W : 서쪽으로 주어진 칸만큼 이동합니다.
# E : 동쪽으로 주어진 칸만큼 이동합니다.