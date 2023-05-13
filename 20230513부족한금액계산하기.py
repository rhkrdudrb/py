#  https://school.programmers.co.kr/learn/courses/30/lessons/82612

def solution(price, money, count):
    price_sum = 0
    p = price
    for i in range(count): 
        price_sum += p
        p += price
    return max(price_sum - money, 0)
    answer = price_sum - money
    if answer < 0:
        answer = 0 
    return answer
print(solution(3,20,4)) # result 10
# 3 + 6 + 9 + 12 = 30, 40 -> 0
