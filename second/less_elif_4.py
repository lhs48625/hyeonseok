total = 30000
is_member = False

# (:)콜론은 다음으로
# if는 뒤에 탭키를 눌러서 들여쓰기를 해야됨 
if total <0:
    message = "금액 오류"
# total이 0보다 작으면 금액오류
elif total >= 30000 or is_member:
    message = "무료배송"
# 다음 조건 total이 3000원보다 크거나 같으면  참
else:
    message = "배송비 3000원"

print(message)

#or은 둘다 참이어야 참, and는 둘중 하나만 참이면 참, 
# not는 참,거짓을 반대로 바꿔줌