import streamlit as st

st.title("캐시사용 계산")

@st.cache_data(ttl=60)
def sum_squares(score):
    return sum(range(1, score + 1))
#range 하나씩 꺼내서 반복
# for과 in / for은 반복문의 시작 in은 score안에서

score = st.number_input("1부터 마지막숫자까지 더하기",  min_value=1, max_value=10000, value=1)
if st.button("계산"):

    with st.spinner("계산중"):
        result = sum_squares(int(score))

    st.metric("더한값", result)

if st.button("함수 캐시 지우기"):

    sum_squares.clear()
    st.success("캐시를 지웠습니다.")

st.title("계산기")
with st.form("my_form"):
    st.subheader("더하기계산기")
    num1 = st.number_input("첫번째 숫자 : ", min_value=1, max_value=10000)
    num2 = st.number_input("두번째 숫자 : ", min_value=1, max_value=10000)
    submitted = st.form_submit_button("더하기계산")
    if submitted:
        num3 = num1 + num2
        st.info(num3)



with st.form("my_form1"):
    num1 = st.number_input("첫번째 숫자 : ", min_value=1, max_value=10000)
    num2 = st.number_input("두번째 숫자 : ", min_value=1, max_value=10000)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        submitted = st.form_submit_button("더하기계산")
    with col2:
        submitted1 = st.form_submit_button("빼기계산")
    with col3: 
        submitted2 = st.form_submit_button("곱하기계산")
    with col4:
        submitted3 = st.form_submit_button("나누기계산")
    if submitted:
        num3 = num1 + num2
        st.info(num3)
    if submitted1:
        num3 = num1 - num2
        st.info(num3)
    if submitted2:
        num3 = num1 * num2
        st.info(num3)
    if submitted3:
        num3 = num1 / num2
        st.info(num3)



with st.form("my_form2"):
    num1 = st.number_input("첫번째 숫자 : ", min_value=1, max_value=10000)
    num2 = st.number_input("두번째 숫자 : ", min_value=1, max_value=10000)