from collections import deque
def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sum_q1 = sum(queue1)
    sum_q2 = sum(queue2)
    cnt = 0
    while sum_q1 != sum_q1: #같을때까지
        # 큐1 빼고 큐2 추가 합큐1에 - 합큐2에 +   
    return answer
# [3,2,7,2]
# [4,6,5,1]
2,7,2 -> 11
4,6,5,1,3 ->
print(solution([3, 2, 7, 2]	[4, 6, 5, 1]))    # 2
print(solution([1, 2, 1, 2]	[1, 10, 1, 2]))   # 7
print(solution([1, 1]	[1, 5]))                # -1
