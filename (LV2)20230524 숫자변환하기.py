# https://school.programmers.co.kr/learn/courses/30/lessons/154538
def solution(x, y, n):
    answer = 0
    sumarry = []
    # ss= 0
    x1 = x
    x2 = x 
    x3 = x
    while True:
        if y in sumarry:    # y가 만들어 지는 경우
            return answer
        # for num in sumarry: 
        #      if num > y:
        #             return -1 
        if x1+n <= y:
            sumarry.append(x1+n)
            x1 +=n
        if x2*2 <= y:
            sumarry.append(x2*2)
            x2 *=2
        if x3*3 <= y:
            sumarry.append(x3*3)  
            x3 *=3
        print(sumarry)
        answer += 1  
        # print(answer)
        # ss += 1
   
#     ----------------------------------------------------------
#     answer = 0
#     seq1 = list(step1(x,y,n))
#     seq2 = list(step2(x,y))
#     seq3 = list(step3(x,y))
#     if seq1[1] != y:
#         seq1[0] = float("inf")
#     if seq2[1] != y:
#         seq2[0] = float("inf")
#     if seq3[1] != y:
#         seq3[0] = float("inf")    
#     if seq1[0] == float("inf") and seq2[0] == float("inf") and seq3[0] == float("inf") :
#         return -1
#     return min(seq1[0],seq2[0],seq3[0])
# def step1 (x_num,y_num,n_num):
#     answer = x_num
#     cnt = 0
#     while y_num > answer:
#         answer += n_num
#         cnt += 1
#     return cnt,answer

# def step2 (x_num,y_num):
#     answer = x_num
#     cnt = 0
#     while y_num > answer:
#         answer *=2
#         cnt += 1
#     return cnt,answer

# def step3 (x_num,y_num):
#     answer =x_num
#     cnt = 0
#     while y_num > answer:
#         answer *=3
#         cnt += 1
#     return cnt,answer

print(solution(10,40,5))   # 2
print(solution(10,40,30))  # 1
print(solution(2,5,4))     # -1



# x : 10, y: 40, n: 5
# 10 15 20 25 30 35 40
# 15 30 45 60


