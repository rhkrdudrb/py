# https://school.programmers.co.kr/learn/courses/30/lessons/42584
from collections import deque
def solution(prices):
    answer = []
    prices = deque(prices)
    while len(prices):
        num = prices.popleft()
        cnt = 0
        for number in prices:
            cnt += 1
            if num > number: #계속증가하다 다음것이 더 작으면 break
                break
        answer.append(cnt)        
    return answer

print(solution([1, 2, 3, 2, 3])) #4 3 1 1 0
print(solution([1, 2, 3, 4, 5, 2]))#	[5, 4, 3, 2, 1, 0]
print(solution([2, 2, 3, 1, 5]))#	3, 2, 1, 1, 0
