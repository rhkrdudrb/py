# https://school.programmers.co.kr/learn/courses/30/lessons/120923
# import math
def solution2(num, total):
    result = []
    avg = total / num
    if num%2 == 1:
        start = avg - num // 2 
        aaaaaa = start + num
        for i in range(int(start), int(start) + num): 
            result.append(i)
        return result
    else: 
        ceil = avg - num/2    #3.5 - 2 = 1.5 3.5 앞뒤 2개 씩 
        start = math.ceil(ceil) # 1.5 올림 시작값:2
        for u in range(start,start +num): 
            result.append(u)
    return result
print(solution2(3,12))

#     print(temp)
#     answer = temp
#     return answer
# num, total => 
# 3, 12
# [3, 4, 5], [n-1, n, n + 1]
# 5 15
# [1,2,3,4,5], [n-2, n-1, n, n + 1, n + 2]
# 7, 21
# [0,1,2,3,4,5,6], [n-3, n-2, n-1, n, n + 1, n + 2, n+3]
# 3 => n-1
# 5 => n-2
# 7 => n-3
# a => n-(num // 2)
# 짝수
# 4	14	
# [2, 3, 4, 5], [n-1, n, n+1, n+2]

# [1 2] [n]
# [n-1 n n+1] : 3n
# [n-2 n-1 n n+1 n+2] : 5n

# 4, 14, 14 / 4 = 3.5
# [2 3 4 5]
# start, end , end - start = num
# end = start + num
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# https://school.programmers.co.kr/learn/courses/30/lessons/120924
# def solution(common):
#     #등차수열 -> 일정하게 더해지는 수열 -> 검색함
#     #등비수열 -> 일정하게 곱해지는 수열 -> 검색함
#     #[1, 2, 3, 4]
#     #[2, 4, 8]
#     #common[1] - common[0] == common[2] - common[1]
#     if common[1] - common[0] == common[2] - common[1] : #2-1 == 3-2 ==> 등차가 같다 그럼 등차수열
#          return common[-1] + (common[1] - common[0])   #4+(2-1) =5
#     return common[-1] * (common[1] / common[0])   #8*(4/2) =16
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
# if s == word[:len(s)]: # 
# def solution(babbling):
#     answer = 0
#     hi = ["aya", "ye", "woo", "ma"]
#     for word in babbling:
#         for s in hi:
#             if s == word[:len(s)]: # 
#                  word = word.replace(s,'?')        #i를 hi를 ?으로 치환한다   
#         print("치환된 아이"+word.strip('?'))
#         if word.strip('?') == '':          #?으로만 있는문자는 모두 발음이 된다 판단하에 ?을 공백으로 치환후 answer +1
#                 answer += 1    
#     return answer
# def solution(babbling):
#     answer = 0
#     hi = ["aya", "ye", "woo", "ma"]
#     for word in babbling:
#         for s in hi:
#             if s == word[len():len(s)]:
#                  word = word.replace(s,'')
                 
#         if word == '':          #?으로만 있는문자는 모두 발음이 된다 판단하에 ?을 공백으로 치환후 answer +1
#                  answer += 1         
#     return answer
# https://school.programmers.co.kr/learn/courses/30/lessons/120956
 def solution(babbling):
    answer = 0
    hi = ["aya", "ye", "woo", "ma"]
    for word in babbling:
        while len(word) > 0:
            changed = False
            for h in hi:
                if word[:len(h)] == h:
                    word = word[len(h):]
                    changed = True
                    break
            if not changed:
                 break            
        if len(word) == 0:          #?으로만 있는문자는 모두 발음이 된다 판단하에 ?을 공백으로 치환후 answer +1
                answer += 1    
    return answer
print(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]))
# def solution(babbling):
#     answer = 0
#     hi = ["aya", "ye", "woo", "ma"]
#     for word in babbling:
#         while len(word) > 0:
#             if word[:3] == 'aya':
#                 word = word.replace('aya','',len(word[:3]))
#             elif word[:2] == 'ye':
#                 word = word.replace('ye','',len(word[:2]))
#             elif word[:3] == 'woo':
#                 word = word.replace('woo','',len(word[:3]))
#             elif word[:2] == 'ma':
#                 word = word.replace('ma','',len(word[:2]))
#             else:
#                 break
#         print("치환된 아이"+word)
#         if len(word) == 0:          #?으로만 있는문자는 모두 발음이 된다 판단하에 ?을 공백으로 치환후 answer +1
#                 answer += 1    
#     return answer
# print(solution(["wooaya"]))
# print(solution(["ayayewoo"]))
# print(solution(3,12))
# print(solution(5,15))
# print(solution(5,5))
# print(solution(4,14))
# print(solution(8,27))
# "aayaayaayaayaayaayaayaayaayaayaayaayaayaayaayaayaayae"
# "aya", "ayanc"
# s = "abcde", s[2:4] = "cd"
#s[:3]
# prefix, word
# prefix == word[:len(prefix)]
# time complexity
# n -> n, n**2, 
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# 20230308 복습
# def solution(babbling):
#     answer = ["aya", "ye", "woo", "ma"]
#     cnt = 0
#     for word in babbling:
#         for letter in answer:
#             word = word.replace(letter,"?") 
#         print(word)
#         if word.strip("?") == "":
#             cnt +=1
#     return cnt



