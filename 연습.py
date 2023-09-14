from collections import defaultdict
def solution(survey, choices):
    answer = ''
    table = defaultdict(int)
    table_arry=[('R','T'),('C','F'),('J','M'),('A','N')]
    for i in range(len(choices)):
        if choices[i] > 4:
            table[survey[i][1]] += choices[i] - 4 
        else:
            table[survey[i][0]] += 4 -choices[i] 
    for i in table_arry:
        if table[i[0]] >= table[i[1]]:
            answer += i[0]
        else:
            answer += i[1]
    return answer
def solution(k, m, score):
    answer = 0
    score.sort(reverse=True) # 외우다 보니 계속 까먹음 기억하기
    arry=[]
    for i in range(0,len(score),m):
        arry.append(score[i:i+m])
    for num in arry:
        if len(num) == m:
            answer += min(num) * len(num)
    return answer
def solution(t,p):
    answer = 0
    int_p = int(p)
    for i in range(0,len(t)-len(p)+1):
        if int(t[i:len(t)+i]) <= int_p:
            answer+=1
    return answer
from heapq import heappush, heappop
def solution(k, score):
    answer = []
    heap = []
    for num in score:
        if len(num) == k and heap[0] < 4:
            heappop(heap)
        if len(num) < k:
            heappush(heap,num)
        answer.append(heap[0])
    return answer
def solution(ingredient):
    answer = 0
    stack = []
    for el in range(len(ingredient)):
        stack.append(el)
        if el == 1 and len(stack) > 4:
            if stack[-4:] == [1,2,3,1]:
                answer+=1
                for i in range(4):
                    stack.pop()
    return answer
def solution(n, m, section):
    answer = 0
    meter = 0
    for num in section:
        if num > meter:
            meter = num + m - 1
            answer+=1
    return answer
def solution(prices):
    answer = []
    stack = []
    for i in range(len(prices-1,-1,-1)):
        num = prices[i]
        while stack and stack[-1][1] >= num:
            stack.pop()
        if len(stack) == 0:
            answer.append(len(prices)-i-1)
        else:
            answer.append(stack[-1][0] - i)
        stack.append((i,num))
    return answer[::-1]
def solution(numbers):
    # answer = []
    # nums = []
    # for num in numbers[::-1]:
    #     while nums and nums[-1] <= num:
    #         nums.pop()
    #     if len(nums) == 0:
    #         answer.append(-1)
    #     else:
    #         answer.append(num[-1])
    #     nums.append(num)
    answer = []
    stack = []
    for num in numbers[::-1]:
        while stack and stack[-1] <= num:
            stack.pop()
        if len(stack) == 0:
            answer.append(-1)
        else:
            answer.append(stack[-1])
        stack.append(num)
    return answer[::-1]
def solution(park, routes):
    board = cr_board(park)
    r,c = start_point(board)
    R = len(board)
    C = len(board[0])
    ewns2drdc = {"N":(-1,0),"S":(1,0),"W":(0,-1),"E":(0,1)}
    for route in routes:
        nr,nc = r,c
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
def solution(board):
    answer = 0 
    R = len(board)
    C = len(board[0])
    for r in range(R):
        for c in range(C):
            if board[r][c] == 1:
                for dr,dc in((-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)):
                    nr,nc = r+dr,c+dc
                    if not(nr < 0 or nr == R or nc < 0 or nc == C):
                        if board[nr][nc] != 1:
                            board[nr][nc] = 2
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] < 1:
                answer+=1
    return answer
from collections import deque
def solution(cards1, cards2, goal):
    queue1 = deque(cards1)
    queue2 = deque(cards2)
    for letter in goal:
        if queue1[0] == letter:
            queue1.popleft()
            queue1.append('None')
        elif queue2[0] == letter:
            queue2.popleft()
            queue2.append('None')
        else:
            return "No"
    return "Yes"
def solution(keymap, targets):
    answer = []
    for target in targets:
        result = 0
        for keym in target:
            min = float('inf')
            for word in keymap:
                if min > word.find(keym) and word.find(keym) != -1:
                    min = word.find(keym) + 1
            result += min
        if result == float('inf'):
            answer.append(-1)
        else:
            answer.append(result)
    return answer
