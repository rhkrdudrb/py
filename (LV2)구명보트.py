# https://school.programmers.co.kr/learn/courses/30/lessons/42885
from collections import deque

def solution(people, limit):
    answer = 0
    people = deque(sorted(people)) #[]
    while people:
        heavy = people.pop() # 60 
        # if heavy+light > limit:
        if people and heavy + people[0]  <= limit:
            people.popleft()
        answer +=1  # 1 2
    return answer

print(solution([70,50,80,50], 100)) # 3 - (50,50), (70), (80)

print(solution([70,50,30,80,50], 100)) # 3 - (70,30), (50,50), (80)
# 큰수 80 70 50
# 작은수 30 50
# 보트탐 -> 80 70 30 50 50


print(solution([70,50,10,80,50], 100)) # 3 - (70), (50,50), (80, 10)
# 큰수   
# 작은수  
# 보트   80 10 70 50 50

print(solution([20,60,40,80,60], 100)) # (80,20)(60,40)(60) 3


# pseudo- code

