# https://school.programmers.co.kr/learn/courses/30/lessons/176963
from collections import defaultdict

def solution(name, yearning, photo):
    answer = []
    name2yearning = defaultdict(int)
    # yearningsum = 0
    for i in range(len(name)):
        name2yearning[name[i]] = yearning[i]
    for p in photo:
        yearningsum = 0
        for name in p:
            # if name in name2yearning:
            yearningsum += name2yearning[name]

        answer.append(yearningsum)
        # yearningsum = 0
    return answer
print(solution(["may", "kein", "kain", "radi"],[5, 10, 1, 3],[["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))
print(solution(["kali", "mari", "don"],[11, 1, 55],	[["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]]))
print(solution(["may", "kein", "kain", "radi"],[5, 10, 1, 3],[["may"],["kein", "deny", "may"], ["kon", "coni"]]))
    
