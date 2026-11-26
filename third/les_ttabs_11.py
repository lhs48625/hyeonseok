import streamlit as st

tab1, tab2, tab3 = st.tabs(["a", "b", "c"])
with tab1:
    st.subheader("신규")
with tab2:
    st.subheader("신규2")
with tab3:
    st.subheader("신규3")
