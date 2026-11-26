import sys
import json

# =====================================
# 1. 앱 시작 화면 및 초기 데이터 설정
# =====================================

print("=== 파이썬 스마트 스토어 & 학습 매니저 ===")
print("프로그램 이름 : python 기초")
print("수업 시간 :", 60)
print("파이썬 실행기 :", sys.executable)

# 상품 카탈로그
products = {"book": 12000, "note": 8000, "pen": 1500, "bag": 25000, "cup": 6000}
#딕셔너리 형식

print("\n초기 상품 목록")
print(products)

# 보유 상품 및 관심 상품
owned_items = {"book", "pen"}
wish_items = {"pen", "bag"}

# 주문 내역 및 회원 정보
order_history = []
profiles = []


# 회원 프로필 함수
def profile(**kwargs):
    return kwargs


# 견적 계산 함수
def quote(price, quantity, shipping=3000):
    total = price * quantity
    return total + shipping


# 여러 금액 합산 함수
def sum_values(*args):
    return sum(args)


# =====================================
# 2. 메인 메뉴 루프
# =====================================

while True:

    print("\n========== 메인 메뉴 ==========")
    print("1. 상품 목록 보기")
    print("2. 주문 담기 및 견적 계산")
    print("3. 수량 일괄 정산 리포트")
    print("4. 보유 vs 관심 상품 비교")
    print("5. 주문 내역 JSON 저장 및 불러오기")
    print("6. 회원 프로필 / 추가 메모 등록")
    print("0. 종료")

    try:
        main = int(input("\n메뉴를 입력하세요 : "))
    except ValueError:
        print("숫자를 입력하세요.")
        continue

    # =================================
    # 메뉴 1. 상품 목록 보기
    # =================================

    if main == 1:

        print("\n=== 상품 목록 보기 ===")

        sorted_items = sorted(products.items(), key=lambda item: item[1], reverse=True)

        print("\n[가격이 비싼 순서]")

        for name, price in sorted_items:
            print(f"{name} : {price:,}원")

        print("\n최고가 상품 :", sorted_items[0])

        print("\n추천 TOP 3")

        for item in sorted_items[:3]:
            print(item)

    # =================================
    # 메뉴 2. 주문 담기 및 견적 계산
    # =================================

    elif main == 2:

        print("\n=== 주문 담기 및 견적 계산 ===")

        name = input("사용자 이름 : ").strip()

        if not name:
            print("이름을 입력하세요.")
            continue

        member_input = input("회원 여부 (y/n) : ").strip().lower()

        if member_input not in ("y", "n"):
            print("y 또는 n을 입력하세요.")
            continue

        is_member = member_input == "y"

        item_input = input("주문할 상품 (예: book,pen) : ").strip()

        item_names = [item.strip() for item in item_input.split(",") if item.strip()]

        if not item_names:
            print("상품을 입력하세요.")
            continue

        # 상품 존재 여부 확인
        unknown_items = [item for item in item_names if item not in products]

        if unknown_items:
            print("등록되지 않은 상품 :", unknown_items)
            continue

        # 수량 입력 및 예외 처리
        try:
            quantity = int(input("수량 : "))

            if quantity <= 0:
                print("수량은 1 이상이어야 합니다.")
                continue

        except ValueError:
            print("정수를 입력하세요.")
            continue

        # 상품별 금액 계산
        item_totals = [products[item] * quantity for item in item_names]

        # *args 함수로 누적 금액 계산
        subtotal = sum_values(*item_totals)

        # 배송비 조건
        if subtotal >= 30000 and is_member:
            shipping = 0
            message = "무료배송"
        else:
            shipping = 3000
            message = "배송비 3000원"

        # 최종 견적 계산
        total = quote(subtotal, 1, shipping)

        print("\n========== 주문 견적 ==========")
        print("주문자 :", name)
        print("회원 여부 :", is_member)
        print("주문 상품 :", item_names)
        print("상품별 금액 :", item_totals)
        print("상품 합계 :", f"{subtotal:,}원")
        print("배송 안내 :", message)
        print("최종 결제 금액 :", f"{total:,}원")

        # 주문 내역 저장
        order = {
            "name": name,
            "is_member": is_member,
            "items": item_names,
            "quantity": quantity,
            "subtotal": subtotal,
            "shipping": shipping,
            "total": total,
        }

        order_history.append(order)

    # =================================
    # 메뉴 3. 수량 일괄 정산 리포트
    # =================================

    elif main == 3:

        print("\n=== 수량 일괄 정산 리포트 ===")

        try:
            input_data = input("수량 리스트 입력 (예: 2,3,0,-1,1) : ")

            quantities = [int(n.strip()) for n in input_data.split(",")]

        except ValueError:
            print("정수를 입력하세요.")
            continue

        # 0 이하의 수량 제외
        totals = [n * 8000 for n in quantities if n > 0]

        # enumerate를 이용한 딕셔너리 컴프리헨션
        report = {str(i + 1): value for i, value in enumerate(totals)}

        print("\n정산 금액 리스트 :", totals)
        print("정산 리포트 :", report)

        print("전체 정산 금액 :", f"{sum_values(*totals):,}원")

    # =================================
    # 메뉴 4. 보유 vs 관심 상품 비교
    # =================================

    elif main == 4:

        print("\n=== 보유 vs 관심 상품 비교 ===")

        # 교집합
        print("보유 및 관심 상품 :", sorted(owned_items & wish_items))

        # 차집합
        print("보유만 한 상품 :", sorted(owned_items - wish_items))

        # 합집합
        print("전체 상품 :", sorted(owned_items | wish_items))

    # =================================
    # 메뉴 5. JSON 저장 및 불러오기
    # =================================

    elif main == 5:

        print("\n=== JSON 저장 및 불러오기 ===")

        # 현재 데이터 요약
        summary = {
            "orders": order_history,
            "profiles": profiles,
            "owned_items": sorted(owned_items),
            "wish_items": sorted(wish_items),
        }

        # JSON 문자열로 변환
        text = json.dumps(summary, ensure_ascii=False, indent=4)

        print("\n[JSON 저장 데이터]")
        print(text)

        # JSON 문자열 다시 복원
        restored = json.loads(text)

        print("\n[JSON 불러오기 및 검증]")

        print("주문 내역 :", restored["orders"])
        print("회원 정보 :", restored["profiles"])
        print("보유 상품 :", restored["owned_items"])
        print("관심 상품 :", restored["wish_items"])

        # 복원 데이터 검증
        if restored == summary:
            print("\nJSON 데이터 복원 성공!")
        else:
            print("\nJSON 데이터 복원 실패!")

    # =================================
    # 메뉴 6. 회원 프로필 / 추가 메모 등록
    # =================================

    elif main == 6:

        print("\n=== 회원 프로필 / 추가 메모 등록 ===")

        name = input("회원 이름 : ").strip()

        if not name:
            print("이름을 입력하세요.")
            continue

        try:
            level = int(input("회원 등급 번호 : "))
        except ValueError:
            print("등급은 정수로 입력하세요.")
            continue

        state = input("회원 등급 (bronze/silver/gold) : ").strip()

        memo = input("추가 메모 : ").strip()

        # **kwargs를 이용한 프로필 생성
        member = profile(name=name, level=level, state=state, memo=memo)

        profiles.append(member)

        print("\n[등록된 회원 프로필]")
        print(member)

        print("\n[전체 회원 목록]")

        for p in profiles:
            print(p)

    # =================================
    # 메뉴 0. 프로그램 종료
    # =================================

    elif main == 0:

        print("\n프로그램을 종료합니다.")
        break

    # =================================
    # 잘못된 메뉴 입력
    # =================================

    else:
        print("잘못된 메뉴입니다. 다시 입력하세요.")
