# https://school.programmers.co.kr/learn/courses/30/lessons/160586
def solution(keymap, targets):
    answer = []
    for target in targets: # targets: ["ABCD", "AABB"], target: "ABCD"
        result = 0
        for keym in target: # keym:"A","B","C","D"
            min = float('inf')
            for ss in keymap: # ss: "ABACD", keymap: ["ABACD", "BCEFD"]
                if min > ss.find(keym) and ss.find(keym) != -1:
                    min = ss.find(keym)
            result += min
        answer.append(result)
    return answer
print(solution(["ABACD","BCEFD"],["ABCD", "BCEFD"])) # [9,4]
# keymap
# ["ABACD", "BCEFD"]	["ABCD"]
# A -> 1
# B -> 1
# C -> 2
# D -> 5
# 1 + 1 + 2 + 5
# "BCEFD".index("A") >> error
# find >> -1
# -1 일때
