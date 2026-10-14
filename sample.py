import json
import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore

# 1. 입력 폼 만들기

with st.form("diary_input"):
    content = st.text_input("오늘의 일기")
    submit = st.form_submit_button("기록하기")

    if submit and content:
        db.collection("diary").add({"text": content, "date": "2024-05-20"})
        st.success("저장 완료!"); st.rerun()

# 2. 목록 출력 및 삭제

docs = db.collection("diary").stream()
for doc in docs:
    col1, col2 = st.columns([8, 2])
    col1.info(doc.to_dict()["text"])
    if col2.button("삭제", key=doc.id):
        db.collection("diary").document(doc.id).delete()
        st.rerun()