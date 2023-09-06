from collections import defaultdict
def solution(survey, choices):
    answer = ''
    table = defaultdict(int)
    table_arry=[('R','T'),('C','F'),('J','M'),('A','N')]
    for i in range(len(choices)):
        if choices[i] > 4:
            table[survey[i][1]] += choices[i] - 4 
        else:
            table[survey[i][0]] += 4 -choices[i] 
    for i in table_arry:
        if table[i[0]] >= table[i[1]]:
            answer += i[0]
        else:
            answer += i[1]
    return answer
def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    arry=[]
    for i in range(0,len(score),m):
        arry.append(score[i:i+m])
    for num in arry:
        if len(num) == m:
            answer += min(num) * len(num)
    return answer
def solution(t,p):
    answer = 0
    int_p = int(p)
    for i in range(0,len(t)-len(p)+1):
        if int(t[i:len(t)+i]) <= int_p:
            answer+=1
    return answer
from heapq import heappush, heappop
def solution(k, score):
    answer = []
    heap = []
    for num in score:
        if len(num) == k and heap[0] < 4:
            heappop(heap)
        if len(num) < k:
            heappush(heap,num)
        answer.append(heap[0])
    return answer
def solution(ingredient):
    answer = 0
    stack = []
    for el in range(len(ingredient)):
        stack.append(el)
        if el == 1 and len(stack) > 4:
            if stack[-4:] == [1,2,3,1]:
                answer+=1
                for i in range(4):
                    stack.pop()
    return answer
def solution(n, m, section):
    answer = 0
    meter = 0
    for num in section:
        if num > meter:
            meter = num + m - 1
            answer+=1
    return answer
def solution(prices):
    answer = []
    stack = []
    for i in range(len(prices-1,-1,-1)):
        num = prices[i]
        while stack and stack[-1][1] >= num:
            stack.pop()
        if len(stack) == 0:
            answer.append(len(prices)-i-1)
        else:
            answer.append(stack[-1][0] - i)
        stack.append((i,num))
    return answer[::-1]
def solution(numbers):
    # answer = []
    # nums = []
    # for num in numbers[::-1]:
    #     while nums and nums[-1] <= num:
    #         nums.pop()
    #     if len(nums) == 0:
    #         answer.append(-1)
    #     else:
    #         answer.append(num[-1])
    #     nums.append(num)
    answer = []
    stack = []
    for num in numbers[::-1]:
        while stack and stack[-1] <= num:
            stack.pop()
        if len(stack) == 0:
            answer.append(-1)
        else:
            answer.append(stack[-1])
        stack.append(num)
    return answer[::-1]