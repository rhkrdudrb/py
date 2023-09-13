# https://school.programmers.co.kr/learn/courses/30/lessons/160586
def solution(keymap, targets):
    for target in targets:
        result = 0
        for keym in target:
            min = float('inf')
            for word in keymap:
                if min > word.find(keym) and word.find(keym) != -1:
                    min = word.find(keym) + 1
            result += min 
        if result == float('inf'):
            answer.append(-1)
        else:
            answer.append(result)
    return answer
------------------------------------------------------------------
from collections import defaultdict
def solution(keymap, targets):
    answer = []
    letter2cnt = create_letter2cnt(keymap)
    for target in targets: # targets: ["ABCD", "AABB"], target: "ABCD"
        result = 0
        for letter in target: # keym:"A","B","C","D"
            if letter not in letter2cnt:
                result = -1
                break
            result += letter2cnt[letter] # 1 + 1 + 2 + 5
        answer.append(result)
    return answer
print(solution(["ABACD", "BCEFD"],["ABCD", "AABB"])) # [9,4]
print(solution(["AA"], ["B"])) # [-1]	
print(solution(["AGZ", "BSSS"], ["ASA", "BGZ"])) # [4,6]
	

def create_letter2cnt(keymap): # ["ABACD", "BCEFD"]
    letter2cnt = {}
    for word in keymap: # ABACD, BCEFD
        for i,letter in enumerate(word,1): # A, B, A, C, D
            if letter in letter2cnt: #키가 딕셔너리에 있냐? (문법)
                if letter2cnt[letter] > i :
                    letter2cnt[letter] = i
            else: 
                letter2cnt[letter] = i #A -> 1, B->1, C->2 ,D-> 5 | E-> 3, F->4 
    return letter2cnt
# A -> 1
# B -> 1
# C -> 2
# D -> 5

# keymap
# ["ABACD", "BCEFD"]	["DDDDD"]
# A -> 1
# B -> 1
# C -> 2
# D -> 5
# 1 + 1 + 2 + 5
# "BCEFD".index("A") >> error
# find >> -1
# -1 일때
