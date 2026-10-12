import streamlit as st

st.title("혼자 만드는 웹앱2")

name = st.text_input("아이디")
password = st.text_input("비밀번호")
btn = st.text_input("확인")

col1, col2, col3 = st.columns(3)

with st.form("my_form"):
    with col1:
        submit1 = st.form_submit("나의 일정")
    with col2:
        submit2 = st.form_submit("나의 계획")
    with col3:
        submit3 = st.form_submit("나의 미래")