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
            queue2.popleft() #popleft 리스트의 pop(0)이랑 같은 기능이지만 시간은O(1) 리스트의 pop(0) 은 길이에 따라 소요시간 달라질수 있음
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
    
