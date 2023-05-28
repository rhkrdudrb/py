# https://school.programmers.co.kr/learn/courses/30/lessons/154538
def solution(x, y, n):
    answer = 0
    seq1 = step1(x,y,n)
    seq2 = step2(x,y)
    seq3 = step3(x,y)
    print(seq1)
    print(seq2)
    print(seq3)
    if seq1[1] == y or seq2[1] == y or seq3[1] == y :
        return min(seq1[0],seq2[0],seq3[0])
    else:
        return -1
def step1 (x_num,y_num,n_num):
    answer = x_num
    cnt = 0
    while y_num > answer:
        answer += n_num
        cnt += 1
    return cnt,answer

def step2 (x_num,y_num):
    answer = x_num
    cnt = 0
    while y_num > answer:
        answer *=2
        cnt += 1
    return cnt,answer

def step3 (x_num,y_num):
    answer =x_num
    cnt = 0
    while y_num > answer:
        answer *=3
        cnt += 1
    
    return cnt,answer

# x 10  y 60  n 5

# 10 15 20 25 30 35 40 45 50 55 60 -->10
# 10 20 40 60 -> 3
# 10 30 60 -> 2

print(solution(10,40,5))   # 2
print(solution(10,40,30))  # 1
print(solution(2,5,4))     # -1



# x : 10, y: 40, n: 5
# 10 15 20 25 30 35 40
# 15 30 45 60


