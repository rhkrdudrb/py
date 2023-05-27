# https://school.programmers.co.kr/learn/courses/30/lessons/154539
def solution(numbers):
    nums = []
    answer = []
    for num in numbers[::-1]:
        # if len(nums) == 0:
        #     answer.append(-1)
        # elif num < nums[-1]:
        #     answer.append(nums[-1])
            
        while nums and nums[-1] <= num:
            nums.pop()
        if len(nums) == 0:
            answer.append(-1)
        else:
            answer.append(nums[-1])
        nums.append(num)
    return answer[::-1]
print(solution([2, 3, 3, 5]))       # [3, 5, 5, -1]
print(solution([9, 1, 5, 3, 6, 2])) # [-1, 5, 6, 6, -1, -1]


[2,3,3,5]

nums: [5,3,2]
answer: [-1,5,5,3]


[9, 1, 5, 3, 6, 2]

nums: [] 
answer: [-1,-1,6,6,5,-1]