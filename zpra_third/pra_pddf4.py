
import pandas as pd
import streamlit as st

# 제목 출력
st.title("과목의 평균 출력")

# 과목별 점수 데이터 만들기
rows = [
    {"subject": "국어", "score": 90},
    {"subject": "영어", "score": 80},
    {"subject": "수학", "score": 100}
]

# 데이터프레임 만들기
df = pd.DataFrame(rows)

# 전체 평균 계산하기
avg = df["score"].mean()

# 데이터 표 출력하기
st.dataframe(df, hide_index=True)

# 과목별 점수를 막대그래프로 출력하기
st.bar_chart(df.set_index("subject")["score"])

# 전체 평균 출력하기
st.metric("전체 평균", f"{avg:.2f}점")
