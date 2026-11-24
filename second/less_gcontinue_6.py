total = 0
for number in range(1, 11):
     # range는 반복 / 1에서 10까지
    if number % 2 != 0:
        #홀수인지 확인
        continue
    #홀수이면 아래 코드를 실행하지않고 다음반복으로 이동
    total += number
    print(total)
# 1~10사이에 숫자중
# 짝수만 골라 합계를 구함