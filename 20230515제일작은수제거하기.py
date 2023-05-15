# https://school.programmers.co.kr/learn/courses/30/lessons/12935
def solution(arr):
    answer = []
    min_arry =arr[0]
    for i in arr:
        if i < min_arry:        
            min_arry = i
    del arr[arr.index(min_arry)]
    answer = arr
    if len(answer) <= 1:
        return [-1]
    return answer
print(solution([4,3,2,1]))
print(solution([10]))


