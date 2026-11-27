from pathlib import Path
# pathlib에서 Path 기능 가져오기
# 파일 및 폴더의 경로를 쉽게 관리할 수 있음

import streamlit as st
# Streamlit 라이브러리 가져오기
# 웹 대시보드를 만들 때 사용

from les_qcsv_5 import parse_sales, summarize
# les_qcsv_5.py 파일에서 매출 데이터 처리 함수 가져오기
# parse_sales : CSV 파일을 읽고 데이터로 변환
# summarize : 매출 데이터 요약


st.set_page_config(page_title="매출 대시보드", layout="wide")
# 웹페이지 제목 설정 및 화면 레이아웃을 넓게 설정

st.title("업로드 매출 대시보드")
uploaded = st.file_uploader("UTF-8 CSV", type=["csv"])
# 사용자가 CSV 파일을 업로드할 수 있는 입력창 생성
# "UTF-8 CSV" : 업로드 창에 표시할 안내 문구
# type=["csv"] : CSV 파일만 업로드할 수 있도록 제한

sample = Path(__file__).resolve().parents[1] / "data" / "sales.csv"
# __file__ : 현재 실행 중인 파이썬 파일의 위치
# resolve() : 파일의 절대 경로를 구함
# parents[1] : 현재 파일에서 두 단계 위의 부모 폴더
# / "data" / "sales.csv" : data 폴더 안의 sales.csv 파일을 지정

raw = uploaded.getvalue() if uploaded else sample.read_bytes()
# uploaded가 존재하면 업로드한 CSV 파일을 읽음
# getvalue() : 업로드한 파일의 내용을 바이트(byte)로 가져옴
#
# uploaded가 없으면 기본 sales.csv 파일을 읽음
# read_bytes() : 파일의 내용을 바이트(byte)로 읽음
#
# 조건식의 구조:
# 참일 때 값 if 조건 else 거짓일 때 값

try:
    rows = parse_sales(raw)
    # CSV 파일의 원본 데이터(raw)를 parse_sales 함수에 전달
    # CSV 내용을 분석하여 파이썬에서 사용할 수 있는 데이터로 변환

except ValueError as exc:
    st.error(str(exc))
     # 발생한 오류 내용을 웹페이지에 표시
    # str(exc) : 오류 객체를 문자열로 변환

    st.stop()
    # 오류가 발생했으므로 이후 코드를 실행하지 않고 종료

choices = ["전체"] + sorted({row["product"] for row in rows})
# rows에 들어 있는 모든 상품명을 가져옴
# row["product"] : 각 매출 데이터에서 상품명만 추출
# { } : 중복된 상품명을 제거하기 위한 집합(set)
# sorted() : 상품명을 오름차순으로 정렬
# ["전체"] : 모든 상품을 조회할 수 있는 항목 추가

selected = st.selectbox("상품", choices)
# 웹페이지에 상품 선택 상자 생성
# choices에 저장된 상품 목록을 선택 항목으로 표시
# selected에는 사용자가 선택한 상품명이 저장됨

filtered = rows if selected == "전체" else [
row for row in rows if row["product"] == selected
]
# selected가 "전체"이면 모든 매출 데이터를 가져옴
# 특정 상품을 선택하면 해당 상품의 데이터만 가져옴
# row["product"] == selected
# 각 데이터의 상품명이 선택한 상품명과 같은지 비교
# 조건식:
# rows if selected == "전체"
# else [조건에 맞는 데이터]

summary = summarize(filtered)
# 필터링된 매출 데이터를 summarize 함수에 전달
# 계산된 결과를 summary 변수에 저장
# summary에는 다음과 같은 정보가 들어 있음
# revenue    : 총매출
# quantity   : 총 판매수량
# by_product : 상품별 매출

st.metric("총매출", f"{summary['revenue']:,}원")
# 웹페이지에 총매출을 표시
# summary["revenue"] : 계산된 총매출 금액
# :, : 숫자를 천 단위마다 쉼표로 표시
# f-string : 문자열 안에 변수의 값을 넣는 방법
# 예: 1500000 -> 1,500,000원


st.metric("수량", summary["quantity"])
# summary["quantity"]에 저장된 총 판매수량을 화면에 표시

st.dataframe(filtered)
# filtered에 저장된 매출 데이터를 표 형태로 출력
# 사용자가 선택한 상품에 해당하는 데이터만 표시

if filtered:
    st.bar_chart(summary["by_product"])
    # summary["by_product"]에 저장된 상품별 매출 데이터를
    # 막대그래프 형태로 화면에 표시
    
else:
    st.info("표시할 데이터가 없습니다.")