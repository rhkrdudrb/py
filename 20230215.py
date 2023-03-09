from collections import defaultdict
# https://school.programmers.co.kr/learn/courses/30/lessons/120826
# 특정문자 제거하기 replace 안쓰고 다시 풀기
# 중복된 문자 제거와 유사
def solution3(my_string, letter):
    answer = ""
    for word in my_string:
        if word not in letter:
            answer += word
    return answer
# 20230309 복습
def solution(my_string, letter):
    # answer = my_string.replace(letter,'')
    answer = ''
    for word in my_string:
        if word == letter:
            continue
        else:
            answer += word 
    return answer    
# https://school.programmers.co.kr/learn/courses/30/lessons/120583
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
# 20230309 복습
def solution(array, n):
    answer = 0
    for num in array:
        if num == n:
            answer +=1
    return answer
# https://school.programmers.co.kr/learn/courses/30/lessons/120888
# 중복된 문자 제거
def solution(my_string):
    answer = ""
    visited = set()
    for word in my_string:
        if word not in visited:
            answer +=word
            visited.add(word)
    return answer
print(solution("people"))   
# 20230309 복습
def solution(my_string):
    answer = ''
    for word in my_string:
        if word not in answer:
            answer+=word
    return answer
# https://school.programmers.co.kr/learn/courses/30/lessons/120812    
# 어떤 원소 가 존재하는지 체크하면서 누가 몇개 있는지,순서를 신경 x
# e in "abcdefghijkl" -> len("abcde")
# set, e in set("a", "b", "c", )  -> 
# print(solution("people")) # "peol"
# 최빈값 구하기 데이터구조 파악
# countarray[i], temp[i]
# dictionary : key -> value, letter(한글자) -> count
# [1,2,3,3,4]
# {1: 0}

# d = {}
# d['a'] >> 'a' KeyError
# d = defaultdict(int)
# d['a'] = 0
# [1,1,2,1] 1 -> 3, 2 -> 1
# [1,1,2,1] 1 -> 1
# [1,1,2,1] 1 -> 2
# [1,1,2,1] 1 -> 1, 2 =>1
# [1,1,2,1] 1 -> 3, 2 =>1
def solution2(array):
    max_cnt = -1
    submax_cnt = -1
    max_num = -1
    submax_num = -1
    num2cnt = defaultdict(int)
    for num in array:
        num2cnt[num] += 1   # 1 -> 3, 2 =>1
    for num,cnt in num2cnt.items():
        if max < cnt:
            submax_cnt = max_cnt # -1
            max_cnt = cnt # 1
            submax_num = max_num
            max_num = num
        elif submax_cnt < cnt <= max_cnt:
            submax_cnt = cnt # 1
            submax_num = num
    if submax_cnt == max_cnt:
        return -1 
    return max_num
# 20230309 복습 코드가 난잡함..
from collections import defaultdict
def solution(array):
    answer =0
    key2value = defaultdict(int)
    for num in array:
        key2value[num] += 1
    key =[key for key,value in key2value.items()]    
    value =[value for key,value in key2value.items()]
    maxvalue = max(value)
    
    if len(value) == 1:
        return max(key)
    for val in value:
        if val == maxvalue:
            answer +=1
            if answer >= 2:
                return -1
    for key,value in key2value.items():  
        if value == maxvalue:
            return key
    print(maxvalue)    
    return answer
def solution5(numbers):
    max = -1
    submax = -1             # [3,4,4,2,2]
    for num in numbers: 
        if max < num:
            submax = max  # 3
            max = num      # 4
        elif submax < num <= max: #최고전값
            submax = num  
    return max * submax

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
