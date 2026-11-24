import streamlit as st

st.title("혼자 만드는 웹앱")
st.info("파이썬으로 제작하는 UI")

col1, col2, col3 = st.columns(3)
with col1:
    st.success("왼쪽 영역")
    st.write("안녕하세요")
with col2:
    st.success("가운데 영역")
    st.write("반갑습니다")
with col3:
    st.success("오른쪽 영역")
    st.write("바보입니다")

# 데이터 입력
name = st.text_input("아이디")
password = st.text_input("비밀번호")
btn = st.button("확인")

#폼 입력 & 상태관리

col4, col5 = st.columns(2)

with st.form("my_form"):
    col4, col5 = st.columns(2)
    with col4:
      submit = st.form_submit_button("전송")
    with col5:
      hhh = st.form_submit_button("완성")
    


st.session_state.login = True


#새로고침 시 데이터 유지
if "user_list" not in st.session_state:
    st.session_state.user_list = []

with st.form("input_form"):
    name = st.text_input("이름")
    if st.form_submit_button("등록") and name:
        st.session_state.user_list.append(name)


tasks = [
    "1. 출근하기",
    "2. 퇴근하기",
    "3. 휴가가기"
]

st.subheader("금일 할 일 목록")

for task in tasks:
    # border=true를 주면 각 반복 요소가 단정한 상자로 감싸집니다.
    
    with st.container(border=True):
        st.write(task)

# 페이지 제목 설정
st.title("첫 Streamlit 앱")

# 텍스트 출력

st.write("Streamlit을 이용해 만든 웹 애플리케이션입니다.")

# 사용자 입력 받기

name = st.text_input("이름을 입력하세요:")
btn = st.button("확인하세요")
