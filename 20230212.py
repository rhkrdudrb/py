import math
def solution(num, total):
    avg = total / num 
    ceil = avg - num/2
    result = []
    if num%2 == 1:
        start = avg - num // 2 # 5- (5 // 2 2)
        for i in range(start, start + num): #start부터 시작해서 start+num의 범위까지
            result.append(i)
        return result
    else:
        start = math.ceil(ceil)
        for k in range(start, start + num): 
            result.append(k)
    return result
print(solution(4,14))

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
# def solution(babbling):
#     answer = 0
#     hi = ["aya", "ye", "woo", "ma"]
#     for word in babbling:
#         for s in hi:
#             if s == word[:len(s)]: # 
#                  i = i.replace(s,'?')        #i를 hi를 ?으로 치환한다
#             else :
#                  continue
#         #print("치환된 아이"+i.strip('?'))
#         if word.strip('?') == '':          #?으로만 있는문자는 모두 발음이 된다 판단하에 ?을 공백으로 치환후 answer +1
#                 answer += 1    
#     return answer
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



