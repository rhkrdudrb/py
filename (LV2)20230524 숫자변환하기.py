# https://school.programmers.co.kr/learn/courses/30/lessons/154538
def solution(x, y, n):
    visited = set() #4
    summary = [(0, x)] #[]
    if x==y:
        return 0
    while summary: # while len(summary) != 0: True
        count, x = summary.pop(0) # 0 2 1 4
        if x+n <= y: # 
            if x + n not in visited:
                if x + n == y:
                    return count +1
                visited.add(x+n)
                summary.append((count + 1, x+n))
        if x*2 <= y:
            if x*2 not in visited:
                if x*2 == y:
                    return count +1
                visited.add(x*2)
                summary.append((count + 1, x*2))
        if x*3 <= y:
            if x*3 not in visited:
                if x*3 == y:
                    return count +1
                visited.add(x*3)
                summary.append((count + 1, x*3))
    return -1  

# pop(0) vs pop()

# [1,2,3,4,5,6] : pop(0) >> O(5)
# [1,2,3,4,5,6]: pop(0) >> O(1)
# collections.deque([]) : double ended queue , popleft() == pop(0)

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


