# https://school.programmers.co.kr/learn/courses/30/lessons/154539
def solution(numbers):
    for i in range(len(numbers)-1):
        changed = True
        for j in range(i+1,len(numbers)):
            if numbers[i] < numbers[j] :
                numbers[i] = numbers[j]
                changed = False
                break
        if changed :
            numbers[i] = -1
    numbers[-1] = -1
    return numbers
print(solution([2, 3, 3, 5]))       # [3, 5, 5, -1]
print(solution([9, 1, 5, 3, 6, 2])) # [-1, 5, 6, 6, -1, -1]






