from heapq import heappush, heappop, heapify
# https://school.programmers.co.kr/learn/courses/30/lessons/142085
def solution(n, k, enemy): #n 병사 k 무적권 enemy 라운드
    answer = 0
    # 무적권
    heap = []
    temp = []
    for idx, e in enumerate(enemy):
        if idx <= k: # idx: 0, k: 3
            heappush(heap,  e) 
            continue
        temp.append(e)
    heap_n = heappop(heap)
    if n >= heap_n:
        n-=heap_n
        answer += 1
    else:
        return k
    for e in temp:
        if n >= e:
            n -= e
            answer+=1
        else:
            break
    return answer + k
# ------------------------------------------------------
# def solution(n, k, enemy): #n 병사 k 무적권 enemy 라운드
#     answer = 0
#     # 무적권
#     heap = []
#     for idx, e in enumerate(enemy):
#         if idx <= k: # idx: 0, k: 3
#             heappush(heap,  e) 
#             continue
#         # answer: 4
#         # [4,2,4,5]
#         n -= heappop(heap)
#         if n >= e : #라운드 통과 () ()
#             n -= heappop(heap)
#             answer+=1
#     return answer + k
# #                   #     #  #  
# print(solution(7,3,[4, 2, 4, 5, 3, 3, 1,10]))   # 5 
# print(solution(7,3,[8, 8, 8, 8, 3, 3, 1,10]))   # 3

# k랑 비교 


# heap : min-heap - priority queue 숫자가 작을수록 priority가 높음
heap = heapify([3,2,5,6,7])
heappop(heap) # 2
heappop(heap) # 3
heappush(heap, 1)
heappop(heap) # 1
heap[0] # min
heap[1] # 2번째로 작은 값이 아니다

# heap - max-heap
heap = heapify([-3,-2,-5,-6,-7])
heappop(heap) # -7 => 7
heappop(heap) # -6 => 6
