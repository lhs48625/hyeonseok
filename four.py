import json
import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore

# Firebase 중복 초기화 방지
if not firebase_admin._apps:
    key_string = st.secrets["firebase_key"]
    cred_dict = json.loads(key_string)
    cred = credentials.Certificate(cred_dict)
    firebase_admin.initialize_app(cred)

db = firestore.client()

st.title("혼자 만드는 웹앱2")
st.write("Streamlit을 이용한 웹앱")

name = st.text_input("아이디")
password = st.text_input("비밀번호")

if name and password:
    db.collection("diary").add({"name": name, "password": password, "date": "2026-10-14"})
    st.success("저장 완료!"); st.rerun()
    st.button("로그인하기")
    if name:
        st.success(f"안녕하세요, name")
    else:
        st.warning("아이디, 비밀번호를 입력하세요.")
    


col7, col8, col9, col10 = st.columns(4)
with col7:
    st.button("아이디찾기")
with col9:
    st.button("비밀번호찾기")
with col9:
    st.button("회원가입")
with col10:
    if st.button("로그인하기"):
        if name:
                st.success(f"안녕하세요, {admin}님")
        else:
                st.warning("아이디, 비밀번호를 입력하세요.")


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

st.success("각 시간 별 점수를 넣어주세요")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.text_input("나의 과거")
with col2:
    st.text_input("나의 현재")
with col3:
    st.text_input("나의 미래")
with col4:
    st.text_input("앞으로의 계획")

st.write("등록하기 누른 후 저장하세요.")

col5, col6 = st.columns(2)

with col5:
    if st.button("등록하기"):   
        if name:
            st.success(f"확인되었습니다.")
        else:
            st.warning("빈칸을 넣어주세요.")
with col6:
    if st.button("임시저장"):
        if name:
            st.success(f"임시저장되었습니다.")
        else:
            st.warning("다시시도해주세요.")

