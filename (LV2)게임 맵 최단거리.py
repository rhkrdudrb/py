# https://school.programmers.co.kr/learn/courses/30/lessons/1844
from collections import deque
def solution(maps):
    answer = 0
    R = len(maps)
    C = len(maps[0])
    queue = deque([(0,0)])
    check = set()
    while queue:
        r,c = queue.popleft()
        # print(r,c)
        for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:#상하좌우
            nr,nc = r,c
            if 0 <= nr+dr < R and 0 <= nc+dc < C and maps[nr+dr][nc+dc] != 0 and (nr+dr,nc+dc) not in check:
                check.add((nr+dr,nc+dc))
                queue.append((nr+dr, nc+dc)) #(1,1,6)
                print(nr+dr,nc+dc)
                answer+=1 #answer 값 처리 조건 수정하기 지금 코드는 최단거리가 맞다고함
    return answer
# 모든 수를 하는데 최단거리의 조거은 어떡게..? 
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])) #answer 11
# print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]])) #answer -1
