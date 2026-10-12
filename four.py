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

tasks = [
    "1. 나의 과거",
    "2. 나의 현재",
    "3. 나의 미래",
    "4. 앞으로의 계획"
]

st.subheader("나를 배워보는 시간")

for task in tasks:
    #border=True를 주면 각 반복 요소가 단정한 상자로 감싸집니다.

    with st.container(border=True):
        st.write(task)


col1, col2, col3, col4 = st.coulmns(4)
with col1:
    st.success_text_input("나의 과거")
with col2:
    st.success_text_input("나의 현재")
with col3:
    st.success_text_input("나의 미래")
with col4:
    st.success_text_input("앞으로의 계획")
