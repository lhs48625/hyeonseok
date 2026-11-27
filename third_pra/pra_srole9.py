import streamlit as st

st.title("길이체크")

if "messages" not in st.session_state:
    st.session_state.messages = []

if st.button("초기화"):
    st.session_state.messages = []


question = st.chat_input("질문", max_chars=10)
if question and question.strip():
    st.session_state.messages += [
        {"role": "user", "content": question},
        {"role": "assistant", "content": f"길이: {len(question)}"},
    ]
    st.session_state.messages = st.session_state.messages[-10:]
    #화면에 남아있는 나의 질문, 답변이 10개로 고정
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])








