# https://school.programmers.co.kr/learn/courses/30/lessons/12948
def solution(phone_number):
    return '*'*(len(phone_number)-4) + phone_number[-4:]
    answer = ''
    # for i in range(len(phone_number)):
    #     if i < len(phone_number)-4:
    #         answer += "*"
    #     else:
    #         answer += phone_number[i]

print(solution("01033334444"))
print(solution("027778888"))



