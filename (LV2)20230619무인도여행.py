https://school.programmers.co.kr/learn/courses/30/lessons/154540#qna
from collections import deque
def solution(maps):
    answer = []
    board = []
    # 보드생성
    for s in maps:
        s = list(s)
        board.append(s)
    # 보드 경계
    R = len(board)
    C = len(board[0])
    check_set= set()
    queue = deque([()])
    n_sum = 0
    for i in range(R):
        for j in range(C):
            if board[i][j] != 'X':
                if(i,j) not in check_set:
                    queue = deque([(i, j)])
                    while queue:
                        check = True
                        r, c = queue.popleft()
                        for dr,dc in [(-1,0),(1,0),(0,1),(0,-1)]: # (0,-1) #상,하,우,좌
                            nr,nc = r+dr , c+dc #(0,5)
                            if 0 <= nr <  R and 0 <= nc < C and board[nr][nc] != 'X': #안나가면
                                check = False
                                if (nr,nc) not in check_set:
                                    n_sum += int(board[nr][nc])
                                    queue.append((nr, nc)) #(1,1,6)   
                                    check_set.add((nr,nc))
                        if check:
                            n_sum = int(board[i][j])
                    answer.append(n_sum)
                    n_sum = 0
    if len(answer) != 0 :
        return sorted(answer)
    else:
        return [-1]
# -----------------------------print 있음 ----------------------------------------
from collections import deque
def solution1(maps):
    answer = []
    board = []
    # 보드생성
    for s in maps:
        s = list(s)
        board.append(s)
    # 보드 경계
    R = len(board)
    C = len(board[0])
    check_set= set()
    queue = deque([()])
    n_sum = 0
    for i in range(R):
        for j in range(C):
            if board[i][j] != 'X':
              if (i,j) not in check_set:
                  queue = deque([(i, j)])
                  print("----------------")
                  while queue:
                      check = True
                      print('팝전',queue)
                      r, c = queue.popleft()
                      print('팝후',queue)
                      print('시작점',queue)
                      for dr,dc in [(-1,0),(1,0),(0,1),(0,-1)]: # (0,-1) #상,하,우,좌
                        nr,nc = r+dr , c+dc #(0,5)
                        if 0 <= nr <  R and 0 <= nc < C and board[nr][nc] != 'X': #안나가면
                            check = False
                            if (nr,nc) not in check_set:
                                print('11111',nr,nc)
                                n_sum += int(board[nr][nc])
                                queue.append((nr, nc)) #(1,1,6)   
                                check_set.add((nr,nc))
                                print(check_set)
                                print(queue)
                      print(check)
                      if check:
                          n_sum = int(board[i][j])
                  answer.append(n_sum)
                  n_sum = 0
                  print("*********************") 
    if len(answer) != 0 :
      return sorted(answer)
    else:
      return [-1]
print(solution(["X591X","X1X5X","X231X", "1XXX1"]))
print(solution(["XXX","XXX","XXX"]))
