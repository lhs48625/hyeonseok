import streamlit as st

st.title("과일가게")
st.markdown("맛있는 과일이 있습니다.")

col1, col2 = st.columns(2)
with col1:
    st.header("바나나")
with col2:
    st.header("딸기")
