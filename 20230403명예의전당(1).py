from heapq import heappop, heappush
# https://school.programmers.co.kr/learn/courses/30/lessons/138477
def solution(k, score):
    answer = []
    heap=[]     #명예의 전당
    for num in score:
        if len(heap) == k and heap[0] < num:
            heappop(heap) #가장작은값 빠짐
        if len(heap) < k:
            heappush(heap, num) 
        print(heap[0])
        answer.append(heap[0]) #가장작은값 append
    return answer
def solution(k, score):
    answer = []
    heap = []
    for num in score:
        if lne(heap) == k and heap[0] < num:
            heappop(heap)
        if len(heap) < k:
            heappush(heap, num)
        answer.append(heap[0])

print(solution(3,[10, 100, 20, 150, 1, 100, 200]))

# min(a, b)
# max(a, b)

# [10, 20, 45, 60, 70, 80, 90, 100] , 85
#------------------------------------------------------------------------------
# def solution(k, score):
#     answer = []
#     hall=[]     #명예의 전당
#     for num in score:
#         if len(hall) == k: 
#             if num >= min(hall): #가장 작은값 삭제 및 num 삽입 
#                 hall.remove(min(hall))
#                 hall.append(num)
#                 answer.append(min(hall))
#             else: #num이 명예의 전당 가장작은 값보다 작으므로 answer 작은값 삽입
#                 answer.append(min(hall))
#         else : # k길이까지 명예의 전당 배열 append
#             hall.append(num)
#             answer.append(min(hall))
#     return answer
#------------------------------------------------------------------------------
# min-heap, max-heap
# 첫번쨰애가 제일작음 가장작은 애만 궁금할떄 정렬안되어도 상관없음
# 힙은 특정한 규칙을 가지는 트리로, 최댓값과 최솟값을 찾는 연산을 빠르게 하기 위해 고안된 완전이진트리를 기본으로 한다. 
# 힙 생성 & 원소 추가
# heapq 모듈은 리스트를 최소 힙처럼 다룰 수 있도록 하기 때문에, 빈 리스트를 생성한 후 heapq의 함수를 호출할 때마다 리스트를  인자에 넘겨야 한다.
# 아래 코드는 heap이라는 빈 리스트를 생성하고 50, 10, 20을 각각 추가하는 예시이다.
# import heapq
# heap = []
# heapq.heappush(heap, 50)
# heapq.heappush(heap, 10)
# heapq.heappush(heap, 20)
# print(heap)
# -------------------------------------------------------------------------------------------------------------------------------------------
# 이미 생성해둔 리스트가 있다면 heapify 함수를 통해 즉각적으로 힙 자료형으로 변환할 수 있다.
# heap2 = [50 ,10, 20]
# heapq.heapify(heap2)
# print(heap2)
# -------------------------------------------------------------------------------------------------------------------------------------------
# 힙에서 원소 삭제
# heappop 함수는 가장 작은 원소를 힙에서 제거함과 동시에 그를 결괏값으로 리턴한다.
# result = heapq.heappop(heap)
# print(result)
# print(heap)
# -------------------------------------------------------------------------------------------------------------------------------------------
# 위의 예제의 경우 heap에서 가장 작은 원소인 10이 결과로 리턴되었고, 힙에서는 제거된 것을 볼 수 있다.
# 원소를 삭제하지 않고 가져오고 싶으면 [0] 인덱싱을 통해 접근하면 된다.
# result2 = heap[0]
# print(result2)
# print(heap)
from heap import heappop,heappush
def soultion(k,score):
    answer = []
    heap = []
    for num in score:
        if len(heap) == k and heap[0] < num:
            heappop(heap)
        if len(heap) < k:
            heappush(heap,num)
        answer.appen(heap[0])
    return answer
	