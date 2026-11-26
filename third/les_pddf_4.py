import pandas as pd

# pandas라이브러리를 pd라는 이름으로 불러오기
# 데이터를 표 형태로 만들고 관리할때 사용
import streamlit as st

st.title("상품별 매출")

rows = [
    {"product": "book", "quantity": 2, "price": 12000},
    {"product": "pen", "quantity": 5, "price": 1500},
]
# 상품 데이터를 저장할 리스트 만들기

df = pd.DataFrame(rows)
# pandas의 행, 열 데이터 구조
# 리스트에 저장된 데이터를 판다스 데이터프레임으로 변환하기


df["revenue"] = df["quantity"] * df["price"]
# revenue(새로운 열)
# 계산결과를 매출액으로 저장


st.dataframe(df, hide_index=True)
# 데이터 프레임을 웹화면에 표형태로 출력
# 왼쪽에 표시되는 행 번호 숨기기  hide_index = True


st.bar_chart(df.set_index("product")["revenue"])
# 상품별 매출액을 막대그래프로 표시하기
# set_index("product") : 상품명을 그래프의 가로축 기준으로 설정
# ["revenue"] : 매출액 데이터만 선택

st.metric("총매출", f"{int(df['revenue'].sum()):,}원")
# 전체 매출액 계산하기
# df["revenue"].sum() : 매출액 열의 모든 값을 더하기
# int() : 정수형으로 변환하기
# :, : 숫자에 천 단위 쉼표 표시하기
# f-string을 사용하여 마지막에 원 붙이기


# pd.DataFrame(rows) 데이터를 표로 만들기

# df["revenue"] revenue 열 선택

# df["a"] * df["b"] 두 열을 곱하기

# st.dataframe(df) 표 화면에 출력

# st.bar_chart() 막대그래프 출력

# .sum() 전체 합계 계산
