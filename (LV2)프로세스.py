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
#------------------------------------------------------------------
#max 안쓰고 정렬로 푸는중
from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque(priorities)
    che_queue = deque(sorted(priorities,reverse=True)) 
    check = deque([0 for _ in range(len(priorities))])
    check[location] = 1
    while queue:
        priorities = queue.popleft()
        checkpop = check.popleft()
        check_queue = che_queue.popleft()
        answer+=1
        if queue and priorities < check_queue :
            queue.append(priorities)
            check.append(checkpop)
            che_queue.append(checkpop)
            print(queue)
            print(check)
            print(che_queue)
        else :
            if checkpop == 1:
                return answer
#------------------------------------------------------------------
#max안씀
from collections import deque
def solution(priorities, location):
    answer = 0
    queue = deque(priorities)                             
    #check index
    check = deque([0 for _ in range(len(priorities))])    # 나가는위치 priorities index
    check[location] = 1                                   # 확인해야할 위치 1 나머지 0
    #check max
    check_queue = deque(sorted(priorities,reverse=True))  # 최고값 정렬
    check_queue_pop = check_queue.popleft()               # 최고값
    check_queue.append(1)                                 # (check_queue_pop) pop할떄 에러 못잡아서 더미데이터 넣음..
    while queue:
        priorities = queue.popleft()                      
        checkpop = check.popleft()
        if queue and priorities < check_queue_pop :       # 우선순위가 더 작으면 
            queue.append(priorities)                      # 뒤로 미룸
            check.append(checkpop)                        # 인덱스도 같이 미룸
            continue                                      # 다시위로 안올리면 바로 끝날경우도 있음
        else : 
            answer+=1                                     
            check_queue_pop = check_queue.popleft()       # 우선순위가 크거나 같으니 최고값 pop(여기서 못잡음..)
        if checkpop == 1:                                 # 확인해야할 index 찾으면 answer return
            return answer
print(solution([2, 1, 3, 2],2))        #1
print(solution([1, 1, 9, 1, 1, 1],0))  #5

