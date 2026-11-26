import streamlit as st

st.title("세션 카운터")

if "count" not in st.session_state:
    # count라는 값이 세션 상태에 없으면 0으로 초기화
    st.session_state.count= 0
if st.button("증가"):
    st.session_state.count += 10
if st.button("감소"):
    st.session_state.count = max(0, st.session_state.count - 5)
if st.button("초기화"):
    st.session_state.count = 0
st.metric("현재 값", st.session_state.count)

