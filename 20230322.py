def solution(today, terms, privacies):
    answer = []
    today = string2day(today)#날짜를 일수로
    term2day = {}
    for term in terms:
        term, day = term.split()
        term2day[term] = int(day)*28
    # term2day = {i[:1]:int(i[2:])*28 for i in terms} #딕셔너리로
    for num, privacy in enumerate(privacies, 1): # "2021.05.02 A" 
        day, term = privacy.split()
        startday = string2day(day)
        if startday + term2day[term] <= today:
            answer.append(num)
    return answer

# key -> value
# key2value

def string2day(s):
    year, month, day = s.split(".") # (2022,05,19)
    return 2*28*int(year) +int(month)*28 +int(day)
print(solution("2022.05.19",["A 6", "B 12", "C 3"],["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"])) #[1, 3] 
