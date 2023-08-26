# https://school.programmers.co.kr/learn/courses/30/lessons/12939
def solution(s):
    answer = list(map(int,s.split()))
    min_answer = float('inf')
    max_answer = float('-inf')
    for num in answer: # 1 
        max_answer = max(max_answer, num)
        min_number = min(min_number, num)
        if num > max_answer:
            max_answer = num # 1
        if num < min_answer: #
            min_answer = num 
        
    # return str(min(answer))+' '+str(max(answer))
print(solution("1 2 3 4"))      # "1 4"
print(solution("-1 -2 -3 -4")) 	# "-4 -1"
print(solution("-1 -1")) 	    # "-1 -1"