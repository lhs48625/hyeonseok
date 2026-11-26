import streamlit as st

st.set_page_config(page_title="학습안내", layout="wide")
st.title("개발자반")
#페이즈의 큰 제목


st.markdown("오늘 목표 : 입력과 결과를 구분합니다.")
#markdown 형식의 텍스트 출력


st.sidebar.header("학습 안내")
#사이드바



st.sidebar.write("총 60시간")
left, right = st.columns(2)
#가로로 나뉜 배치영역


with left:
    st.header("입력")
    st.write("왼쪽에서 조건을 고릅니다.")
with right:
    st.header("입력")
    st.write("오른쪽에서 조건을 고릅니다.")