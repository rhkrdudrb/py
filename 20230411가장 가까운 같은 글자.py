# https://school.programmers.co.kr/learn/courses/30/lessons/142086
from collections import defaultdict
def solution(s):
    let2index = defaultdict(int)
    answer = []
    for i,letter in enumerate(s):
        if letter in let2index:
            # key가 있는 경우
            answer.append(i - let2index[letter])
        else:
            # 없는 경우
            answer.append(-1)
        let2index[letter] = i #b-0,a-1,
    return answer
print(solution("banana"))

# b a n a n a
# b -> 0
# a -> 1
# n -> 4
[-1,-1,-1,2,2,2]