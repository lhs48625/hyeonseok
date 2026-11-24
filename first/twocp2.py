students = [{"name": "철수", "score": 85}, {"name": "영희", "score":55}]
for s in students:
    if s["score"] >= 60:
        result = "합격"
    else:
        result = "재시험"
    print(f"{s['name']}, {s['score']}: {result}")





def calculate_stats(score_list):
    total = sum(score_list)
    avg = total / len(score_list)
    return total, avg

total, avg = calculate_stats([90, 80, 100])
print(f"총점: {total}, 평균: {avg:.2f}")