price = 12000
quantity = 3
discount_rate = 0.1
product = "노트"
is_member = True
subtotal = price * quantity
print(product, subtotal)
print(type(price).__name__, type(discount_rate).__name__)
# 던더 더블언더바 type(형)name =실질적인 형의 이름
print(subtotal >= 30000, is_member)
# True값 나오기
print(7 / 2, 7 // 2, 7 % 2)
# / 나누기, //나누고 나온 정수값, % 나누고 남은값
