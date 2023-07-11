# https://school.programmers.co.kr/learn/courses/30/lessons/42587
from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque(priorities)
    check = deque([0 for _ in range(len(priorities))])
    check[location] = 1
    while queue:
        priorities = queue.popleft()
        checkpop = check.popleft()
        if queue and priorities < max(queue) :
            queue.append(priorities)
            check.append(checkpop)
        else :
            answer+=1   
            if checkpop == 1:
                return answer
# print(solution([2, 1, 3, 2],2))
print(solution([1, 1, 9, 1, 1, 1],0))
# list - append, pop : 오른쪽에서 넣고 빼고 가능
# deque - append, appendleft, pop, popleft : 양쪽에서 넣고 뺴고 가능
    # [2, 1, 3, 2], 2 >> 1
    # [(1), 1, 9, 1, 1, 1], 0 >> 
    # [1, 9, 1, 1, 1, (1)]
    # [9, 1, 1, 1, (1), 1]
    # [1, 1, 1, (1), 1], 1
#------------------------------------------------------------------
#MAX함수 안씀
from collections import deque
def solution(priorities, location):
    answer = 0
    queue = deque(priorities)
    check = deque([0 for _ in range(len(priorities))])
    check[location] = 1
    while queue:
        priorities = queue.popleft()
        checkpop = check.popleft()
        bignum = 0
        for num in queue:
             if num > bignum:
                bignum = num
        if queue and priorities < bignum :
            queue.append(priorities)
            check.append(checkpop)
        else :
            answer+=1   
            if checkpop == 1:
                return answer
