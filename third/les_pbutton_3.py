import streamlit as st

st.title("구매 금액 계산")
name = st.text_input("이름")
quantity = st.number_input("수량", min_value=1, max_value=100, value=1)
total = int(quantity) * 8000
st.metric("총액", f"{total:,}원")
#metric은 앞문자열 밑에 들어감
if st.button("인사"):
    st.write(f"안녕하세요, {name.strip() or '학습자'}님")