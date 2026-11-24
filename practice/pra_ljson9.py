import json


student = {"name" : "민수", "subject": "과학"}


text = json.dumps(student, ensure_ascii=False)
#아스키코드 false로 해야지 한국어 / ensure_ascii=False

print(json.loads(text)["name"])



a = {"과학", "수학", "영어", "사회"}
b = {"과학", "수학", "과탐", "사탐"}
print(sorted(a & b))
print(sorted(a - b))
print(sorted(a | b))