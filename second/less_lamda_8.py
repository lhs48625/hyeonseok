def sum_values(*args):
    return sum(args)
# *args는 하나의 튜플로 묶어서 전달받음
# 튜플은 한번 값 생성시 변경불가


def profile(**kwargs):
    return kwargs
# **kwargs 딕셔너리로 묶어서 전달받음 
# 딕셔너리는 키와 값(value)
#ex) 이름 제목 나이 (key
#ex) 홍길동 홍길동전 20 (value

print(sum_values(3, 5, 7))
# 숫자 3개를 더함
print(profile(name="민수", Level="basic"))

items = [("pen", 1500), ("book", 12000)]
#하나의 리스트에 저장 / 각상품은 튜플 형태
print(sorted(items, key=lambda item : item[1], reverse=True))
# sorted는 데이터를 정렬하는 함수
# key=lambda item: item[1] 두번째 값을 기준으로 정렬
# reverse=True 큰 가격부터 작은 가격 순서(내림차순)

