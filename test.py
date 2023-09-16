from collections import defaultdict
from heapq import heappop,heappush
#https://school.programmers.co.kr/learn/courses/30/lessons/118666  성격유형
def solution(survey, choices): # ["AN", "CF", "MJ", "RT", "NA"], [5, 3, 2, 7, 5]
    answer = ''
    table = defaultdict(int)
    table_arry = [('R','T'),('C','F'),('J','M'),('A','N')]
    for i in range(len(choices)):
        if choices[i] > 4:
            table[survey[i][1]] += choices[i] - 4
        else:
            table[survey[i][0]] += 4 - choices[i] 
    for nums in table_arry:
        if table[nums[0]] >= table[nums[1]]:
            answer += nums[0]
        else:
            answer += nums[1]
    return answer
# 1번 지표	라이언형(R), 튜브형(T)
# 2번 지표	콘형(C), 프로도형(F)
# 3번 지표	제이지형(J), 무지형(M)
# 4번 지표	어피치형(A), 네오형(N

# https://school.programmers.co.kr/learn/courses/30/lessons/135808 과일장수
def solution(k, m, score): # 3, 4, [1, 2, 3, 1, 2, 3, 1]
    answer = 0
    score.sort(reverse=True)
    arry = []
    for i in range(0,len(score),m):
        arry.append(score[i:i+m])
    for nums in arry:
        if len(nums) == m:
            answer += min(nums) * len(nums)
    return answer
# https://school.programmers.co.kr/learn/courses/30/lessons/147355 크기가작은부분문자열
def solution(t, p): # "3141592", "271"
    answer = 0 
    int_p = int(p)
    for i in range(0,len(t)-len(p) + 1):
        if int(t[i:len(p)+1]) <= int_p:
            answer +=1
    return answer
# https://school.programmers.co.kr/learn/courses/30/lessons/138477 명예의 전당
def solution(k, score): # 3, [10, 100, 20, 150, 1, 100, 200]
    answer = []
    heap = []
    for num in score:
        if len(heap) == k and heap[0] <= num:
            heappop(heap)
        if len(heap) < k:
            heappush(heap,num)
        answer.append(heap[0])
    return answer
# https://school.programmers.co.kr/learn/courses/30/lessons/133502 햄버거 만들기
def solution(ingredient): # [2, 1, 1, 2, 3, 1, 2, 3, 1]
    answer = 0
    stack = []
    for el in ingredient:
        stack.append(el)
        if el == 1 and len(stack) >= 4:
            if stack[-4:] == [1,2,3,1]:
                answer+=1
                for _ in range(4):
                    stack.pop()
    return answer
# https://school.programmers.co.kr/learn/courses/30/lessons/161989 덧칠하기
def solution(n, m, section): # 8 4 [2,3,6]
    answer = 0
    meter = 0
    for num in section:
        if num > meter:
            meter = num + m - 1
            answer +=1
    return answer
# https://school.programmers.co.kr/learn/courses/30/lessons/154539 뒤에있는 큰수
def solution(numbers): # [2, 3, 3, 5]
    answer = []
    stack = []
    for num in numbers[::-1]:
        while stack and stack[-1] >= num:
            stack.pop()
        if len(stack) == 0:
            answer.appned(-1)
        else:
            answer.append(stack[-1])
        stack.append(num)
    return answer[::-1]

# https://school.programmers.co.kr/learn/courses/30/lessons/42584 주식가격
def solution(prices): # [1, 2, 3, 2, 3]
    answer = []
    stack = []
    for i in range(len(prices)-1,-1,-1):
        num = prices[i]
        while stack and stack[-1][1] <= num:
            stack.pop()
        if len(stack) == 0:
            answer.append(len(prices) -i -1)
        else:
            answer.append(stack[-1][0] -1)
        stack.append((i,num))
    return answer[::-1]
# https://school.programmers.co.kr/learn/courses/30/lessons/120866
def solution(board): # [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]
    answer = 0
    return answer
# 안전지대랑 공원산책, 카드뭉치, 대충만든자판, 전에했던것들
# https://school.programmers.co.kr/learn/courses/30/lessons/172928 공원산책
def solution(park, routes):
    board = cr_board(park)
    r,c = start_point(board)
    R = len(board)
    C = len(board[0])
    ewns2drdc = {'N':(-1,0),'S':(1,0),'W':(0,-1),'E':(0,1)}
    for route in routes:
        nr, nc = r,c
        ewns,n = route.split()
        dr,dc = ewns2drdc[ewns]
        for _ in range(int(n)):
            nr,nc = nr+dr,nc+dc
            if nr < 0 or nr == R or nc < 0 or nc == C or board[nr][nc] == "X":
                nr,nc = r,c
                break
        r,c = nr,nc
    return nr,nc
def cr_board(park):
    board = []
    for s in park:
        board.append(list(s))
    return board
def start_point(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "S":
                return i,j


# https://school.programmers.co.kr/learn/courses/30/lessons/120866 안전지대
def solution(board):
    answer = 0
    R = len(board)
    C = len(board[0])
    for r in range(R):
        for c in range(C):
            if board[r][c] == 1:
                for dr,dc in ((-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)):
                    nr,nc = r+dr,c+dc
                    if 0 <= nr < R and 0 <= nc < C and board[nr][nc] != 1:
                        board[nr][nc] = 2
    for r in range(R):
        for c in range(C):
            if board[r][c] == 0:
                answer+= 1
    return answer
from collections import deque    
# https://school.programmers.co.kr/learn/courses/30/lessons/159994 카드뭉치
def solution(cards1, cards2, goal):
    queue1 = deque(cards1)
    queue2 = deque(cards2)
    for letter in goal:
        if queue1 and queue1[0] == letter:
            queue1.popleft()
        elif queue2 and queue2[0] == letter:
            queue2.popleft()
        else:
            return "No"
    return "Yes"

# https://school.programmers.co.kr/learn/courses/30/lessons/160586 대충만든자판
def solution(keymap, targets):
    answer = []
    for target in targets: #"ABACD"
        result = 0
        for keym in target: # A,B,A,C,D
            min = float('inf')
            for word in keymap:
                if min > word.find(keym)

    return answer
# ["ABACD", "BCEFD"]	["ABCD","AABB"]