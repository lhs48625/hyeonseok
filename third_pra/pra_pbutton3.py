import streamlit as st

st.title("계산기")




with st.form("my"):
    st.header("더하기")
    num = st.number_input("첫번째숫자", min_value=1, value=1)
    num1 = st.number_input("두번째숫자", min_value=1, value=1)
    num2 = int(num) + int(num1)
    submit = st.form_submit_button("더하기 계산")
    if submit:
        num2 = num + num1
        st.metric("더하기 값", num2)


with st.form("my1"):
    st.header("뺴기")
    num3 = st.number_input("첫번째숫자", min_value=1, value=1)
    num4 = st.number_input("두번째숫자", min_value=1, value=1)
    num5 = int(num3) + int(num4)
    st.metric("빼기 값", f"{num5}")


with st.form("my2"):
    st.header("곱하기")
    num6 = st.number_input("첫번째숫자", min_value=1, value=1)
    num7 = st.number_input("두번째숫자", min_value=1, value=1)
    num8 = int(num6) + int(num7)
    st.metric("곱하기 값", f"{num8}")

    
with st.form("my3"):
    st.header("나누기")
    num9 = st.number_input("첫번째숫자", min_value=1, value=1)
    num10 = st.number_input("두번째숫자", min_value=1, value=1)
    num11 = int(num9) + int(num10)
    st.metric("나누기 값", f"{num11}")