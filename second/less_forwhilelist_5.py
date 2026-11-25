total = 0
# total 변수의 초기값을 0으로 설정

for quantity in [1, 0, 4]:
     # 리스트의 값을 하나씩 quantity에 넣으며 반복
    if quantity == 0:
         # quantity의 값이 0인지 확인
        continue
    # 현재 반복을 건너뛰고 다음 값으로 이동
    total += quantity
    # total에 quantity 값을 더함
print(total)

attemps = 1
# attemps 변수의 초기값을 1로 설정
while attemps < 6:
    # attemps가 6보다 작은 동안 반복
    attemps += 1
    # attemps 값에 1을 더함

    if attemps == 2:
        # attemps 값이 2인지 확인
        print(attemps)
        # 조건이 참이면 attemps 값 출력


