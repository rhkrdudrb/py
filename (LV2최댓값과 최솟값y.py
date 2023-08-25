# https://school.programmers.co.kr/learn/courses/30/lessons/12939
def solution(s):
    answer = ''
    answer = list(map(int,s.split()))
    return str(min(answer))+' '+str(max(answer))
print(solution("1 2 3 4"))      # "1 4"
print(solution("-1 -2 -3 -4")) 	# "-4 -1"
print(solution("-1 -1")) 	    # "-1 -1"