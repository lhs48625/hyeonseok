import streamlit as st

st.title("대화연습")

if "message" not in st.session_state:
    st.session_state.message = []
    # 세션 상태에 message가 없으면 빈 리스트 생성

question = st.chat_input("질문")
# 채팅 입력창 생성

if question:
    # 질문을 입력하면 실행

    st.session_state.message.append({
        "role": "user", "content": question
    })
    #  st.session_state.message.append 
    # 질문 내용을 세션 상태 리스트에 저장
    #  "role": "user" 메시지를 보낸 사람 (사용자)
    #  "content": question 사용자가 입력한 내용
for message in st.session_state.message:
    # 저장된 모든 메시지를 하나씩 반복

    with st.chat_message(message["role"]):
        # 메시지 역할에 맞는 채팅창 생성

        st.write(message["content"])
         # 메시지 내용 출력

# not 아니다 
# not in 안에 없다