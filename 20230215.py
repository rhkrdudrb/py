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
def solution(array):
    answer = 0
    count = 0
    countarray = []
    temp = list(set(array))
    maxcount = 0
    for i in temp:
        count = array.count(i)
        countarray.append(count)
    print(countarray.index(max(countarray)))
    maxcount = temp[countarray.index(max(countarray))]
    if len(countarray) ==1:
        return maxcount
    print(countarray)
    countarray = [item for item in countarray if item == max(countarray)] #리스트 컴프리헨션 이용하기
    print(countarray)
    if len(countarray) >1:
        return -1  
    return maxcount
print(solution([1, 2, 3, 3, 3, 4]))