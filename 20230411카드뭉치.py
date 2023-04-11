# https://school.programmers.co.kr/learn/courses/30/lessons/159994
from collections import deque
def solution(cards1, cards2, goal):
    answer = ''
    queue1 = deque(cards1)
    queue2 = deque(cards2)
    for letter in goal: 
        if queue1[0] == letter:
            queue1.popleft()
            queue1.append("none")
        elif queue2[0] == letter :
            queue2.popleft()
            queue2.append("none")
        else:
            return 'No'
    return 'Yes'
# def solution(cards1, cards2, goal):
#     answer = ''
#     for letter in goal:
#         if cards1[0] == letter:
#             del cards1[0]
#             cards1.append("none")
#         elif cards2[0] == letter:
#             del cards2[0]
#             cards2.append("none")
#         else:
#             return 'No'
#     return 'Yes'
    
