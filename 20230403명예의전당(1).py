# https://school.programmers.co.kr/learn/courses/30/lessons/138477
def solution(k, score):
    answer = []
    hall=[]     #명예의 전당
    for num in score:
        if len(hall) == k: 
            if num >= min(hall): #가장 작은값 삭제 및 num 삽입 
                hall.remove(min(hall))
                hall.append(num)
                answer.append(min(hall))
            else: #num이 명예의 전당 가장작은 값보다 작으므로 answer 작은값 삽입
                answer.append(min(hall))
        else : # k길이까지 명예의 전당 배열 append
            hall.append(num)
            answer.append(min(hall))
    return answer
print(solution(3,[10, 100, 20, 150, 1, 100, 200]))