name = input("이름 :").strip()
# strip는 앞뒤 공백 제거

raw_quantity = input("수량 :")

quantity = int(raw_quantity)
# str(문자열)을 정수형으로 바꾸는 것
total = quantity * 8000


print(f"{name}님, 총액 :{total:,}원")
# f는 변수값을 문장안에 넣는 문자열
# , 쉼표는 값을 천원단위로

print("book,pen".split(","))
# split (이걸)기준으로 문자열 자르기
