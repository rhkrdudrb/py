from dateutil.relativedelta import relativedelta
import datetime
def solution(today, terms, privacies):
    answer = []
    print(today)
    print(terms)
    print(privacies)
    print('-------------------')
    today = 12*28*int(today[:4]) +int(today[5:7])*28 +int(today[8:11]) #날짜를 일수로
    for k,v in privacies.items():
        print(terms.keys)
    print(terms)
    print(privacies)
    return answer
print(solution("2022.05.19",["A 6", "B 12", "C 3"],["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"])) #[1, 3]