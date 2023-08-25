# https://school.programmers.co.kr/learn/courses/30/lessons/154539
# 외움
def solution(numbers):
    answer = []
    nums = []
    for num in numbers[::-1]:
        while nums and nums[-1] <= num:
            nums.pop()
        if len(nums) == 0:
            answer.append(-1)
        else:
            answer.append(num[-1])
        nums.append(num)
    return answer[::-1]
#------------------------------------------------------------
def solution(numbers):
    nums = []
    answer = []
    for num in numbers[::-1]:
        while nums and nums[-1] <= num: #5
            nums.pop()
        if len(nums) == 0:
            answer.append(-1) # -1
        else:
            answer.append(nums[-1]) #5
        nums.append(num) # 5 3
    return answer[::-1]
print(solution([2, 3, 3, 5]))       # [3, 5, 5, -1]
print(solution([9, 1, 5, 3, 6, 2])) # [-1, 5, 6, 6, -1, -1]
# i: 5 3 3 2
# nums: [5,3]
# answer: [-1,5,5,3]

# [2,3,3,5]

# nums: [5,3,2]
# answer: [-1,5,5,3]


# [9, 1, 5, 3, 6, 2]

# nums: [] 
# answer: [-1,-1,6,6,5,-1]
