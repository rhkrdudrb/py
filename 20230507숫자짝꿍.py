from collections import defaultdict

def solution(X, Y):
    xnum2cnt = defaultdict(int)
    ynum2cnt = defaultdict(int)
    for num in X:
        xnum2cnt[num] += 1
    for num in Y:
        ynum2cnt[num] += 1
    print(xnum2cnt)
    print(ynum2cnt)
    num2cnt = {}
    for key in xnum2cnt:
        if key in ynum2cnt:
            num2cnt[key] 

    answer = ''
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
    