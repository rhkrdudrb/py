# https://school.programmers.co.kr/learn/courses/30/lessons/42584
from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)
    while len(prices):
        num = prices.popleft()
        cnt = 0
        for number in prices:
            if num < number:
                cnt +=1
            else:
                cnt = 1
        answer.append(cnt)        


    return answer

# [1, 2, 3, 2, 3]	[4, 3, 1, 1, 0] 4 3 1 1 0
# [1, 2, 3, 4, 5, 2]	[5, 4, 3, 2, 1, 0]

# 떨어지면 무조건 1 안떨어지면 남은 길이 만큼 올름?