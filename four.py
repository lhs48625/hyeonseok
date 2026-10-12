import streamlit as st

st.title("혼자 만드는 웹앱2")
st.write("Streamlit을 이용한 웹앱")

name = st.text_input("아이디")
password = st.text_input("비밀번호")
btn = st.button("확인")
if st.button("확인"):
    if name:
        st.success(f"안녕하세요, {admin}님")
    else:
        st.warning("이름을 입력하세요")


if "user_list" not in st.session_state:
    st.session_state.user_list = []

