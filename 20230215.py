# 특정문자 제거하기
# def solution(my_string, letter):
#     return my_string.replace(letter,'')
# 중복된 숫자 개수
# def solution(array, n):
#     answer = 0
#     for word in array:
#         if word == n:
#             answer +=1
#     return answer
# 중복된 문자 제거
# def solution(my_string):
#     answer = ''
#     for word in my_string:
#         print(word)
#         if word not in answer:
#             answer +=word
#             #print(answer)
#     return answer
# 최빈값 구하기
def solution(my_string):
    answer = ''
    for word in my_string:
        print(word)
        if word not in answer:
            answer +=word
            #print(answer)
    return answer