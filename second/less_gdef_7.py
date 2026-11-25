def quote(price, quantity, shipping=3000):
    # quote 함수 정의 (가격, 수량, 배송비 / 배송비 기본값은 3000원)
    subtotal = price * quantity
    # 가격 × 수량으로 상품 금액 계산
    return subtotal + shipping
    # 금액에 배송비를 더한 후 결과 반환


total = quote(8000, 3)
# 가격 8000원, 수량 3개 전달 (배송비는 기본값 3000원 사용)

print(total)
print(quote(8000, 3, shipping=0))
# 배송비를 0원으로 지정하여 총금액 출력