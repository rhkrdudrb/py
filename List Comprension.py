# https://bio-info.tistory.com/28 참고 
# 리스트 컴프리헨션은 직관적으로 리스트를 생성하는 방법입니다. 
# 대괄호 "[", "]"로 감싸고 내부에 for문과 
# if 문을 사용하여 반복하며 조건에 만족하는 것만 리스트로 생성할 수 있습니다.
# 0부터 4 뽑는 리스트
li=[]
for i in range(5):
    li.append(i)
# 리스트 컴프리헨션은 사용 후 코드 
[i for i in range(5)]    


t = [(0,3)]

if (2,3) in t:
    print("1111111")
else:
    print("3 in tuple : False")


if (2,3) not in t:
    print("222222")
else:
    print("3 not in tuple : False")