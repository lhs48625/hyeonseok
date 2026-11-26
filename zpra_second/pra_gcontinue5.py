total = 0
for number in range(1, 11):
    if number % 2 != 0:
        # 나누고 남은 값이 1이면 건너뜀
        continue
    total += number
print(total)
# 짝수 값 2,4,6,8,10을 순서대로 더함


print()
total1 = 0
for number1 in range(1, 11):
    if number1 % 2 == 0:
        # 나누고 남은 값이 0이면 건너뛰고 다시 for문으로
        continue
    total1 += number1
    # total1 + number1 = total1
    # ex ) 0+1=1, 1+3=4, 4+5=9
print(total1)
# 홀수 값 1,3,5,7,9를 순서대로 더함

print()

total = 0
number = 1

while number <= 10:
    if number % 2 != 0:
        total += number

    number += 1
print(total)
# 홀수만 더하기
