from collections import defaultdict

# 특정문자 제거하기 replace 안쓰고 다시 풀기
# 중복된 문자 제거와 유사
def solution3(my_string, letter):
    answer = ""
    for word in my_string:
        if word not in letter:
            answer += word
    return answer
# my_string	letter	result
# "abcdef"	"f"	"abcde"
# "BCBdbe"	"B"	"Cdbe"
# 중복된 숫자 개수
def solution4(array, n):
    answer = 0
    for word in array:
        if word == n:
            answer +=1
    return answer
# 중복된 문자 제거
def solution(my_string):
    answer = ""
    visited = set()
    for word in my_string:
        if word not in visited:
            answer +=word
            visited.add(word)
    return answer
# 어떤 원소 가 존재하는지 체크하면서 누가 몇개 있는지,순서를 신경 x
# e in "abcdefghijkl" -> len("abcde")
# set, e in set("a", "b", "c", )  -> 
# print(solution("people")) # "peol"
# 최빈값 구하기 데이터구조 파악
# countarray[i], temp[i]
# dictionary : key -> value, letter(한글자) -> count
# [1,2,3,3,4]
# {1: 0}
def solution2(array):
    num2cnt = defaultdict(int)
    for num in array:
        num2cnt[num] += 1
    # max(num2cnt.values()) # [1,1,2,1]
    numkey = list(num2cnt.keys())
    numvalue = max(num2cnt.values())
    print(numkey)
    print(numvalue)
    if len(num2cnt.values()) == 1:   # [1,1,2,1]
        return max(num2cnt.values())
    if len(max(num2cnt.values)) > 1:
        return -1
    return
    # num2cnt # {1: 1, 2:1, 3:2, 4:1}
    
    # answer = 0
    # count = 0
    # countarray = []         
    # temp = list(set(array)) # 리스트의 집합(중복허용 x)
    # maxcount = 0            # 최빈값
    # for i in temp:          # array의 집합의 갯수구함
    #     count = array.count(i)
    #     countarray.append(count) 
    # print(temp)
    # print(countarray)
    # maxcount = temp[countarray.index(max(countarray))] #array의 집합의 갯수의 인덱스 구해서 temp의 최빈값 구함
    # if len(countarray) ==1: 
    #     return maxcount 
    # countarray = [item for item in countarray if item == max(countarray)] #max값 만 추출
    # if len(countarray) >1: # 최빈값 2개면 -1 return
    #     return -1  
    # return maxcount
print(solution2([1, 2, 3, 3, 3, 4]))
print(solution2([1, 2, 2, 3, 3, 4])) # -1
# d = {}
# d['a'] = 3
# print(d)

# 파이썬 set, dictionary 타입 공부해오기
# https://school.programmers.co.kr/learn/courses/30/lessons/120847
# https://school.programmers.co.kr/learn/courses/30/lessons/120825
# 폰 앱으로 접속
# meet code: iwr-pkie-vkn
# 코드는 깃헙에 올려서 깃헙 링크 전달
