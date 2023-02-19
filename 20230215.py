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
    temp = list(set(array)) # 리스트의 집합(중복허용 x)
    maxcount = 0            # 최빈값
    for i in temp:          # array의 집합의 갯수구함
        count = array.count(i)
        countarray.append(count) 
    print(temp)
    print(countarray)
    maxcount = temp[countarray.index(max(countarray))] #array의 집합의 갯수의 인덱스 구해서 temp의 최빈값 구함
    if len(countarray) ==1: 
        return maxcount 
    countarray = [item for item in countarray if item == max(countarray)] #max값 만 추출
    if len(countarray) >1: # 최빈값 2개면 -1 return
        return -1  
    return maxcount
print(solution([1, 2, 3, 3, 3, 4]))