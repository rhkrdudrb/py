# https://school.programmers.co.kr/learn/courses/30/lessons/120585
def solution(array, height):
    answer = 0
    for numarray in array:
        if numarray > height:
            answer += 1
    return answer

# https://school.programmers.co.kr/learn/courses/30/lessons/120811
def solution(array):
    answer = 0
    array.sort()
    return array[len(array)//2]
# https://school.programmers.co.kr/learn/courses/30/lessons/120893

# https://school.programmers.co.kr/learn/courses/30/lessons/120895