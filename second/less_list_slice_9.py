items = ["book", "pen", "bag"]

print(items[0], items[-1])
#[0]은 0인덱스를 호출해줘 / [-1]은 왼쪽에서 첫번째인덱스를 호출해줘

print(items[1:3])
# 1인덱스부터 3인덱스 미만까지 호출해줘

items.append("cup")
# items 리스트 마지막에 cup을 추가해줘

items[0] = "note"
# items[0] 0인덱스(book)를 note로 변경해줘
#  
print(items)

point = (10, 20)
x, y = point
print(x, y)

# 리스트는 값 변경 가능