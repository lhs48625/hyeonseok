import sys
import json

print("python 기초")
print("수업시간", 60)
print("실행기", sys.executable)

def profile(**kwargs):
    return kwargs
profile(name9 = "book", level=12000)
profile(name9 = "note", level=8000)
profile(name9 = "pen", level=1500)
profile(name9 = "bag", level=25000)
profile(name9 = "cup", level=6000)

args = [
    ("book", 12000),
    ("note", 8000),
    ("pen", 1500),
    ("bag", 25000),
    ("cup", 6000),
]
print(args)


owned_items = {"book", "pen", "book"}
wish_items = {"pen", "bag"}
print(sorted(owned_items & wish_items))
print(sorted(owned_items - wish_items))
print(sorted(owned_items | wish_items))


while True:
    print(1, "상품 목록 보기")
    print(2, "주문 담기 및 견적 계산")
    print(3, "수량 일괄 정산 리포트")
    print(4, "보유 vs 관심 상품 비교")
    print(5, "주문 내역 json 저장 및 불러오기")
    print(6, "회원 프로필 / 추가 메모 등록")
    print(0, "종료")
    
    
    main = 1, 2, 3, 4, 5, 6, 0
    main = input("메뉴를 입력하세요 : ")
    main1 = int(main)

    if main1 == 1:
     list1 = [("book", 12000), ("note", 8000), ("pen", 1500), ("bag", 25000), ("cup", 6000)]
     print(sorted(list1, key=lambda item : item[1], reverse=True))
     print(list1[3], list1[:3])

#########*************************



    if main1 == 2:
     name = input("이름 : ").strip()
     name2 = input("회원여부 y/n : ")
     name3 = input("주문할 상품 : ").split(",")
    if main1 == 2:
        try:
            name4 = int(input("수량 : "))
        except ValueError:
             print("정수를 입력하세요")
        else:
            print(f"{name}님, 회원: {name2}, 상품 :{name3}, 수량: {name4}")

        
        def quote(price, quantity, shipping=3000):
            subtotal = price * quantity
            return subtotal + shipping
        
        is_member = False
        total = 45000
        if total >= 30000 and is_member:
            message = "무료배송"
        else:
            message = "배송비 3000원"

        print(total)
        print(quote(8000, 3, shipping=0))
        def sum_values(*args):
            return sum(args)
        print(sum_values(5000, 5000, 7000))

    
    if main1 == 3:
        args = [2, 3, 0, -1, 1]
        totals = [n * 2000 for n in args if n > 0]
        report = {str(i + 1): v for i, v in enumerate(totals)}
        print(totals)
        print(report)


    if main1 ==4:
        print(sorted(owned_items & wish_items))
        print(sorted(owned_items - wish_items))
        print(sorted(owned_items | wish_items))


    if main1 == 5:
        list = {"list1": "book", "list2": "pen", "list3": "bag"}
        text = json.dumps(list, ensure_ascii=False)
        print(json.loads(text)["list1"])
        print(json.loads(text)["list2"])
        print(json.loads(text)["list3"])

        

    if main1 == 6:
        point = (10, 20)
        x, y = point
        print(x, y)
    if main1 ==6:
        def profile1(**kwargs):
            return kwargs
        print (profile1(nam = "홍길동", lev=1, state = "bronze"))
        print(profile1(nam = "황진이", lev=2, state = "diamond"))
        print(profile1(nam = "두꺼비", lev=3, state = "silver"))
        print(profile1(nam = "거북이", lev=2, state = "gold"))
        print(profile1(nam = "토끼", lev=3, state = "silver"))


    if main1 == 0:
        print("종료")
        break
