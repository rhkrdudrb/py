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
# 문자열은 인덱스로 접근이 가능하나 인덱스로 수정이 불가하여 list로 바꿈
# ex) my_string[num1] = my_string[num2] 안됨 
def solution(my_string, num1, num2):
    answer = list(my_string)
    index = answer[num1]
    answer[num1] = answer[num2]
    answer[num2] = index
    return "".join(answer)
