from collections import deque
def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sum_q1 = sum(queue1)
    sum_q2 = sum(queue2)
    n = len(queue1)
    total = sum_q1 + sum_q2
    if total % 2:
        return -1 
    cnt = 0
    while sum_q1 != sum_q2 and cnt < 4*n: #같을때까지 4*n 아직도 이해못함
            while sum_q1 > sum_q2:
                num = queue1.popleft()
                queue2.append(num)
                sum_q1 -= num
                sum_q2 += num 
                cnt += 1
            while sum_q1 < sum_q2:
                num = queue2.popleft()
                queue1.append(num)
                sum_q2 -= num
                sum_q1 += num 
                cnt += 1
    if cnt >= 4*n:
        return -1
    else:
        return cnt
# [3,2,7,2,4] : 18
# [6,5,1] : 12

print(solution([3, 2, 7, 2]	[4, 6, 5, 1]))    # 2
print(solution([1, 2, 1, 2]	[1, 10, 1, 2]))   # 7
print(solution([1, 1]	[1, 5]))              # -1
print(solution([1]	[2]))                     # -1
print(solution([3]	[6]))                     # -1
print(solution([2,3]	[2,6]))                     # -1

print(solution([1,1]	[2,6]))                     # -1
print(solution([5,7]	[2,8]))                     # -1
1 1 2
6
sum 1 4 
sum 2 6 

7
2 8 5
sum 1 7 
sum 2 15

7 2
8 5
sum 1 9 
sum 2 13

7 2 8
5
sum 1 17
sum 2 5

2 8
5 7
sum 1 10
sum 2 12

2 8 5
7
sum 1 15
sum 2 7
#qu 1 -> 1 1 1
#qu 2 -> 2

#qu 1 -> 1
#qu 2 -> 1 1 2