# https://school.programmers.co.kr/learn/courses/30/lessons/131128
from collections import defaultdict
# def solution(X, Y):
#     answer = ''
#     xnum2cnt = defaultdict(int)
#     ynum2cnt = defaultdict(int)
#     # x 딕셔너리
#     for num in X:
#         xnum2cnt[num] += 1
#     # y 딕셔너리
#     for num in Y:
#         ynum2cnt[num] += 1
#     num2cnt = defaultdict(int)
#     # x,y키값이 같고 그중 작은값
#     for num,cnt in xnum2cnt.items():
#         if num in ynum2cnt:
#             if xnum2cnt[num] > ynum2cnt[num]:
#                 num2cnt[num] = ynum2cnt[num]
#             else:
#                 num2cnt[num] = cnt
#     # 짝꿍이 존재하지 않으면
#     if not num2cnt:
#         return "-1"
#     # 0으로만 구성되어 있다면
#     elif len(num2cnt) == 1 and "0" in num2cnt:
#         return "0"
#     # 그외 정상적인 경우면
#     for num,cnt in num2cnt.items():
#         for num2 in range(cnt):
#             answer+=num
#     return "".join(sorted(answer,reverse=True))
# -----------------------------------sorded 안쓰고-------------------------------------------------------
def solution(X, Y):
    answer = ''
    xnum2cnt = defaultdict(int)
    ynum2cnt = defaultdict(int)
    # x 딕셔너리
    for num in X:
        xnum2cnt[num] += 1
    # y 딕셔너리
    for num in Y:
        ynum2cnt[num] += 1
    num2cnt = defaultdict(int)
    # x,y키값이 같고 그중 작은값
    for num,cnt in xnum2cnt.items():
        if num in ynum2cnt:
            if xnum2cnt[num] > ynum2cnt[num]:
                num2cnt[num] = ynum2cnt[num]
            else:
                num2cnt[num] = cnt
    # 짝꿍이 존재하지 않으면
    if not num2cnt:
        return "-1"
    # 0으로만 구성되어 있다면
    elif len(num2cnt) == 1 and "0" in num2cnt:
        return "0"
# ---------------------------------------------
    # 그 외 경우라면
    for i in range(10,-1,-1):
        key = str(i)
        if key in num2cnt:
            answer += key*num2cnt[key]
# ---------------------------------------------
    return answer
print(solution("100", "2345"))
    # 103 
    # 310 
#   x     y
# "100"	"2345"	"-1"
# "100"	"203045"	"0"
# "100"	"123450"	"10"
# "12321"	"42531"	"321"
# "5525"	"1255"	"552"
5:3 2:1   1:1 2:1 5:2

# 0 -> 0, 0
# 1 -> 0, 1
# 2 -> 1, 1
# 3 -> 0, 0
# ...
# 9

# 100
# 0 -> 2
# 1 -> 1
100
0 2
1 1
2 0
3 0
...
# count, find, del s[:] 이런 애들은 쓰지 않는다
# string의 길이가 n일 때 0부터 9까지 각 숫자가 몇번 들어가는지 세려면 10*n 돌아야 한다
# for i in range(9):
#     xnum2cnt[i] += 1
# n번만 돌면 된다
for i in range(9):
    xnum2cnt[i] = X.count(i)
for num in X:
    xnum2cnt[num] += 1
    
