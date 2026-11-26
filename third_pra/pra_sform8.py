import streamlit as st

with st.form("my_form"):
    email = st.text_input("이메일", value="@")
    people = st.number_input("인원수", min_value=1, max_value=10 ,value=1)
    submitted = st.form_submit_button("계산")
if submitted:
    st.session_state.pop("result", None)
    #pop는 딕셔너리에서 특정 값을 삭제
    try:
        people1 = int(people)
        if "@" not in email.strip():
            raise ValueError("@를 확인하세요")
        if not people:
            raise ValueError("1~10의 숫자만 입력하세요")
        
        st.session_state.result1 = email
        st.session_state.result = people1
        

    except ValueError as e:
        st.error(e)
if "result1" in st.session_state and "result" in st.session_state:
    st.metric("이메일", f"{st.session_state.result1}")
    st.metric("인원수", f"{st.session_state.result}")
