from dateutil.relativedelta import relativedelta
import datetime
def solution(today, terms, privacies):
    answer = []
    print(today)
    print(terms)
    print(privacies)
    print('-------------------')
    today = datetime.datetime.strptime(today,"%Y.%m.%d")
    terms = {i[:1]:today+relativedelta(months=int(i[2:])) for i in terms}

    privacies= {i[11:]:datetime.datetime.strptime(i[:10],"%Y.%m.%d")for i in privacies}
    for k,v in privacies.items():
        print(terms.keys)
    print(terms)
    print(privacies)
    return answer
print(solution("2022.05.19",["A 6", "B 12", "C 3"],["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"])) #[1, 3]