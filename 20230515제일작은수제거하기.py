# https://school.programmers.co.kr/learn/courses/30/lessons/12935
def solution(arr):
    if len(arr) == 1:
        return [-1]
    min_idx = 0
    for idx in range(len(arr)):
        if arr[idx] < arr[min_idx]:        
            min_idx = idx
    return arr[:min_idx] + arr[min_idx+1:]
# [4,3,2,1], min_idx: 1
# [4] + [2,1] = [4,2,1]
print(solution([4,3,2,1]))
print(solution([10,11])) # [11]
print(solution([10])) # [-1]
print(solution([1])) # [-1]



