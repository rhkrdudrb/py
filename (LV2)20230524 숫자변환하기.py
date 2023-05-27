# https://school.programmers.co.kr/learn/courses/30/lessons/154538
def solution(x, y, n):
    answer = 0
    seq1 = step1(x,y,n)
    seq2 = step2(x,y)
    seq3 = step3(x,y)
    if seq1 == float("inf") and seq2 == float("inf") and seq3 == float("inf"):
        return -1
    return min(seq1,seq2,seq3)
def step1 (x_num,y_num,n_num):
    answer = 0
    cnt = 0
    while y_num > answer:
        answer += x_num+n_num
        cnt += 1
    print('일번',answer)
    if answer != y_num:
        return float("inf")
    return cnt
def step2 (x_num,y_num):
    answer = 0
    cnt = 0
    while y_num > answer:
        answer += x_num*2
        cnt += 1
    print('이번',answer)
    if answer != y_num:
        return float("inf")
    return cnt
def step3 (x_num,y_num):
    answer = 0
    cnt = 0
    while y_num > answer:
        answer += x_num*3
        cnt += 1
    print('삼번',answer)
    if answer != y_num:
        return float("inf")
    return cnt
print(solution(10,40,5))   # 2
print(solution(10,40,30))  # 1
print(solution(2,5,4))     # -1



# x : 10, y: 40, n: 5
# 10 15 20 25 30 35 40
# 15 30 45 60


