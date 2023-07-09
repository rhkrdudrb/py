# https://school.programmers.co.kr/learn/courses/30/lessons/1844
from collections import deque
from heapq import heappop, heappush, heapify
def solution(maps):
    R = len(maps)
    C = len(maps[0])
    queue = heapify([(0,0,0)]) # distance, r, c
    check = set()
    while queue:
        d,r,c = heappop(queue)
        if r == R-1 and c == C-1:
            return d
        # print(r,c)
        for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:#상하좌우
            nr,nc = r,c
            if 0 <= nr+dr < R and 0 <= nc+dc < C and maps[nr+dr][nc+dc] != 0 and (nr+dr,nc+dc) not in check:
                check.add((nr+dr,nc+dc))
                heappush(queue, (d + 1, nr+dr, nc+dc)) #(1,1,6)
                print(nr+dr,nc+dc)
    
    return -1
print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])) #answer 11 
# print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]])) #answer -1

[[1,2,3],
[2,3,1],
[4,3,5]]
# 2,2 , R,C = 3,3