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
        answer.append(heap[0])
    return answer


print(solution(3,[10, 100, 20, 150, 1, 100, 200]))

# min(a, b)
# max(a, b)

[10, 20, 45, 60, 70, 80, 90, 100] , 85

# min-heap, max-heap
# 첫번쨰애가 제일작음 가장작은 애만 궁금할떄 정렬안되어도 상관없음
