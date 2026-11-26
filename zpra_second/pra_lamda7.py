def basket_total(*price):

    return sum(price)


print(basket_total(5000, 6000, 7000, 8000, 9000))
#튜플로 묶어서

# ---------------------------------------------------


def basker_total1(**kwargs):
    return kwargs


print(basker_total1(name="수박", sell=5000))
#딕셔너리
# --------------------------------------------------


total = [
    ("수박", 5000),
    ("딸기", 6000),
    ("바나나", 7000),
    ("파인애플", 8000),
    ("귤", 9000),
]

print(sorted(total, key=lambda total: total[0], reverse=True))
#람다 - 간략한 익명함수형식처리 (입력과 출력)
#reverse=True - 큰것부터 작은순서
#reverse=False - 작은것부터 큰순서

