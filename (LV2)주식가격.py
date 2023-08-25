# https://school.programmers.co.kr/learn/courses/30/lessons/42584
from collections import deque
#안보고
def solution(prices):
    answer = []
    nums =[]
    for i in range(len(prices)-1,-1,-1):
        num = prices[i]
        while nums and nums[-1][1] >= num:
            nums.pop()
        if len(nums) == 0:
            answer.append(len(prices)-i-1)
        else:
            answer.append(nums[-1][0] - i)
        nums.append((i,num))
    return answer[::-1]
# -----------------------------------------------------------------------------------------------
def solution(prices):
    answer = []
    nums = [] # (idx, price) []
    for i in range(len(prices)-1, -1, -1): # 3 2 3 2 1, #index 거꾸로
        num = prices[i] # 2 #역순
        while nums and nums[-1][1] >= num: #  nums null and (idx(인덱스),num(가격)) 표현방식
            nums.pop()
        if len(nums) == 0:
            answer.append(len(prices) - i - 1) # prices배열길이 - index - 1 5 - 3 - 1 
        else:
            answer.append(nums[-1][0] - i) #[0, 1, 1, 3, 4]
        nums.append((i,num)) # [(0,1)]
    return answer

# answer 
# 가격이 어느 기간동안 안떨어지는지
print(solution([1, 2, 3, 2, 3])) #4 3 1 1 0, [1,2,3,2,3,2] [5]

print(solution([1, 2, 3, 4, 5, 2]))#	[5, 4, 3, 2, 1, 0]
print(solution([2, 2, 3, 1, 5]))#	3, 2, 1, 1, 0
# -----------------------------------------------------------------------------------------------
#while 한번만
def solution(prices):
    answer = []
    prices = deque(prices)
    check = True
    i = 0
    while len(prices):
        if check:
            num = prices.popleft()
            check_prices = deque(prices)
            i = 0
        if len(check_prices) == 0:
            if len(check_prices) == 0 and len(prices) == 0:
                answer.append(0)
                break
            check = True
            answer.append(i) 
            continue
        check_num = check_prices.popleft()
        i+=1
        check = False
        if num > check_num: 
            check = True
            answer.append(i)
    return answer
print(solution([1, 2, 3, 2, 3])) #4 3 1 1 0
print(solution([1, 2, 3, 4, 5, 2]))#	[5, 4, 3, 2, 1, 0]
print(solution([2, 2, 3, 1, 5]))#	3, 2, 1, 1, 0
# -----------------------------------------------------------------------------------------------
#정답코드
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

# print(solution([1, 2, 3, 2, 3])) #4 3 1 1 0
# print(solution([1, 2, 3, 4, 5, 2]))#	[5, 4, 3, 2, 1, 0]
# print(solution([2, 2, 3, 1, 5]))#	3, 2, 1, 1, 0
