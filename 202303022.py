def solution(today, terms, privacies):
    answer = []
    today = 12*28*int(today[:4]) +int(today[5:7])*28 +int(today[8:11]) #날짜를 일수로
    terms = {i[:1]:int(i[2:])*28 for i in terms} #딕셔너리로
    # privacies={i[-1]:12*28*int(i[:4]) +int(i[5:7])*28 +int(i[8:11]) for i in privacies} 중복떄문에 쓸수없음
    num= 0
    for letter in privacies:
        num += 1
        for key,value in terms.items():
            if letter[-1] == key:
                endday = 12*28*int(letter[:4]) +int(letter[5:7])*28 +int(letter[8:11])
                if endday + value <= today:
                    answer.append(num)
    return answer
print(solution("2022.05.19",["A 6", "B 12", "C 3"],["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"])) #[1, 3]