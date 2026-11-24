import json

student = {"name": "민수", "score": 85}
# name과 score는 키(key)값 민수와 85는 벨류(value)값
student["score"] += 5
print(student.get("city", "미입력"))
# student 변수에서 city가 있다면 출력해주고 없으면 미입력으로 출력

text = json.dumps(student, ensure_ascii=False)
#아스키코드 false로 해야지 한국어 / ensure_ascii=False

print(json.loads(text)["score"])
# json에서 가져오면서 load를 통해서 딕셔너리형으로 변경
# 그래야지 print 할 수 있음

a = {"book", "pen", "book"}
b = {"pen", "bag"}
print(sorted(a & b))
#a와 b에 두 곳다 있는 곳을 보여줘
print(sorted(a - b))
#a와 b를 빼줘 
print(sorted(a | b))
# a와 b를 더해줘

#sorted 데이터를 정렬하는 함수
