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
    check_set= {}
    queue = deque([()])
    for i in range(R):
        for j in range(C):
            if board[i][j] != 'X':
                while queue:
                    print('팝전',queue)
                    queue = deque([(0, i, j)])
                    print('팝후',queue)
                    print('시작점',queue)
                    n_sum, r, c = queue.popleft()
                    for dr,dc in [(-1,0), (1,0), (0,-1), (0,1)]: #상 하 좌 우
                        nr,nc = i,j
                        if 0 < nr or nr == R or 0 < nc or nc == C or board[i][j] == 'X':
                            n_sum += int(board[i][j])
                            queue.append((n_sum,r,c))
                            print(queue)
                        # print(i,j)
                    break
        
    return answer
print(solution(["X591X","X1X5X","X231X", "1XXX1"]))
