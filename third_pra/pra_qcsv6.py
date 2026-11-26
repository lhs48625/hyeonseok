import streamlit as st
from hyeonseok.zpra_third.pra_qcsv5 import parse_sales

st.title("CSV 업로드")
uploaded = st.file_uploader("매출 csv", type=["csv"])
if uploaded is None:
    st.info("data/sales.csv를 선택하세요")
else:
    try:
        rows = parse_sales(uploaded.getvalue())
        st.dataframe(rows)
        st.success(f"{len(rows)}행을 읽었습니다.")
    except ValueError as exe:
        st.error(str(exe))