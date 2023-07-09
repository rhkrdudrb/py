# https://school.programmers.co.kr/learn/courses/30/lessons/42587
from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque(priorities)
    check = []
    while queue:
        bignum = max(queue)
        if queue and queue[0] < bignum :
            check.append((bignum,answer + 1))
            queue.remove(bignum)
        elif queue and  queue[0] >= bignum:
            check.append((queue[0],answer + 1))
            queue.popleft()
        answer+=1   
        print(check)
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
