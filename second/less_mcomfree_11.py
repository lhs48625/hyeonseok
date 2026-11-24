values = [2, 3, 0]
totals =[n * 8000 for n in values if n > 0]
report = {str(i + 1): v for i, v in enumerate(totals)}

print(totals)
print(report)

try:
    quantity = int("abc")
except ValueError:
    print("정수를 입력하세요")