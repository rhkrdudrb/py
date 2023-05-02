# https://school.programmers.co.kr/learn/courses/30/lessons/140108
# 문자열 s가 입력되었을 때 다음 규칙을 따라서 이 문자열을 여러 문자열로 분해하려고 합니다.

# 먼저 첫 글자를 읽습니다. 이 글자를 x라고 합시다.
# 이제 이 문자열을 왼쪽에서 오른쪽으로 읽어나가면서, x와 x가 아닌 다른 글자들이 나온 횟수를 각각 셉니다. 처음으로 두 횟수가 같아지는 순간 멈추고, 지금까지 읽은 문자열을 분리합니다.
# s에서 분리한 문자열을 빼고 남은 부분에 대해서 이 과정을 반복합니다. 남은 부분이 없다면 종료합니다.
# 만약 두 횟수가 다른 상태에서 더 이상 읽을 글자가 없다면, 역시 지금까지 읽은 문자열을 분리하고, 종료합니다.
# 문자열 s가 매개변수로 주어질 때, 위 과정과 같이 문자열들로 분해하고, 분해한 문자열의 개수를 return 하는 함수
def solution(s):
    # 첫글자 구하고(x) x와 x아닌문자 길이 구하기
    s = list(s)
    x = s[0]
    answer = 0
    x_cnt = 0
    other_cnt = 0
    for i,letter in enumerate(list(s)): #x = 1, a =1
        x = s[0] # x 초기화
        if letter == x: # x 카운트
            x_cnt += 1
        else:
            other_cnt += 1 # x 아닌 문자 카운트
        if x_cnt == other_cnt:
            del s[0:int(x_cnt + other_cnt)] # x와 x아닌 문자 길이 만큼 슬라이싱
            answer += 1
            # x와 x아닌 문자 카운트 초기화
            x_cnt = 0
            other_cnt = 0
    if len(s) != 0 : # 슬라이싱 하고 남은 문자도 카운트
        answer +=1
    return answer
print(solution("banana"))
print(solution("abracadabra"))
print(solution("aaabbaccccabba"))
# 입출력 예 #1
# s="banana"인 경우 ba - na - na와 같이 분해됩니다.

# 입출력 예 #2
# s="abracadabra"인 경우 ab - ra - ca - da - br - a와 같이 분해됩니다.

# 입출력 예 #3
# s="aaabbaccccabba"인 경우 aaabbacc - ccab - ba와 같이 분해됩니다.
# banana -> 3
# ba - na - na
# abracadabra -> 6
# ab - ra - ca - da - br - a
# aaabbacc - ccabba -> 3
# 
