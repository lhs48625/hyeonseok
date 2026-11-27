from pathlib import Path
import streamlit as st
import pandas as pd
from posapp1 import parse_sales, summarize

st.set_page_config(page_title="올인원 미니 pos & 매출분석기", layout="wide")

st.title("🏪올인원 미니 POS & 매출 분석기")

if "pos_orders" not in st.session_state:
    st.session_state.pos_orders = []
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "안녕하세요! '총매출', '인기상품', '주문건수' 등을 물어보세요.",
        }
    ]

st.sidebar.header("⚙️ 데이터 관리")
uploaded = st.sidebar.file_uploader("추가 매출 csv업로드(utf-8)", type=["csv"])


@st.cache_data(ttl=60)
def get_cached_summary(rows):
    return summarize(rows)

col1, col2 = st.columns(2)
with col1:
    if st.button("이 함수 캐시 지우기"):
        get_cached_summary.clear()
        st.success("캐시를 초기화했습니다.")
with col2:
    if st.button("POS 입력 내역 초기화"):
        st.session_state.pos_orders = []
        st.sidebar.warning("현장 주문 내역이 초기화되었습니다.")

if uploaded is not None:
    try:
        base_rows = parse_sales(uploaded.getvalue())
        st.sidebar.success(f"CSV에서 {len(base_rows)}행을 불러왔습니다.")
    except ValueError as exc:
        st.sidebar.error(str(exc))
        base_rows = []
else:
    sample_path = Path(__file__).resolve().parent / "data" / "sales.csv"
    if sample_path.exists():
        base_rows = parse_sales(sample_path.read_bytes())
    else:
        base_rows = [
            {"product": "book", "quantity": 2, "price": 12000},
            {"product": "pen", "quantity": 5, "price": 1500},
        ]

all_rows = list(base_rows) + list(st.session_state.pos_orders)

# 탭
tab1, tab2, tab3 = st.tabs(
    ["📊 매출 대시보드", "💳 POS 주문 입력", "💬 매출 도우미 챗봇"]
)


# tab 1
with tab1:
    products = ["전체"] + sorted({row["product"] for row in all_rows})

    selected = st.selectbox("조회할 상품 선택", products)
    if selected == "전체":
        filtered = all_rows
    else:
        filtered = [r for r in all_rows if r["product"] == selected]

    summary = get_cached_summary(filtered)

    # 컬럼
    col3, col4, col5 = st.columns(3)
    with col3:
        st.metric("총매출", f"{summary['revenue']:,}원")
    with col4:
        st.metric("총 판매 수량", f"{summary['quantity']:,}개")
    with col5:
        st.metric("거래 건수", f"{len(filtered)}건")

    # 컬럼
    left, rigth = st.columns([1.2, 1])
    with left:
        st.subheader("상세 거래 내역")
        if filtered:
            df = pd.DataFrame(filtered)
            df["subtotal"] = df["quantity"] * df["price"]
            st.dataframe(df, use_container_width=True, hide_index=True)
        else:
            st.info("표시할 데이터가 없습니다.")
    with rigth:
        st.subheader("상품별 매출 비중")
        if summary["by_product"]:
            st.bar_chart(summary["by_product"])


# tab 2
with tab2:
    st.subheader("신규 현장 주문 등록")
    with st.form("pos_form", clear_on_submit=True):
        p_name = st.text_input("상품명 (1~40자)")

        # 컬럼
        c1, c2 = st.columns(2)

        p_qty = c1.number_input("수량", min_value=1, max_value=1000, value=1)
        p_price = c2.number_input(
            "단가 (원)", min_value=100, max_value=1_000_000, value=5000, step=500
        )

        # 서브버튼
        submitted = st.form_submit_button("주문 추가")
        if submitted:
            clean_name = p_name.strip()

            if not clean_name or len(clean_name) > 40:
                st.error("상품명은 공백 제외 1~40글자로 입력하세요.")
            else:
                st.session_state.pos_orders.append({
                    "product": clean_name,
                    "quantity": int(p_qty),
                    "price": int(p_price),
                })
                st.success(
                    f"'{clean_name}' {p_qty}개 (총 {p_qty * p_price:,}원) 주문이 등록되었습니다! 대시보드 탭에서 확인하세요."
                )


# tab3
with tab3:
    st.subheader("데이터 기반 간단 Q&A")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    prompt = st.chat_input(
        "매출에 대해 질문해보세요 (예: 총매출 알려줘, 가장 잘 팔린 상품은?)"
    )

    if prompt and prompt.strip():
        st.session_state.messages.append({"role": "user", "content": prompt})

        total_summary = get_cached_summary(all_rows)

        if "총매출" in prompt or "매출" in prompt:
            reply = f"현재 누적 총매출은 **{total_summary['revenue']:,}원**입니다."

        elif "인기" in prompt or "가장" in prompt or "상품" in prompt:

            if total_summary["by_product"]:
                best = max(total_summary["by_product"].items(), key=lambda x: x[1])
                reply = f"매출 1위 상품은 **{best[0]}**이며, 총 **{best[1]:,}원**의 매출을 기록했습니다."
            else:
                reply = "아직 등록된 상품 데이터가 없습니다"
        elif "수량" in prompt or "건수" in prompt:
            reply = f"총 거래 건수는 **{len(all_rows)}건**, 총 판매 수량은 **{total_summary['quantity']:,}개**입니다."
        else:
            reply = "질문을 이해하지 못했습니다. **'총매출'**, **'인기 상품'**, **'판매 수량'** 키워드를 포함해 질문해 주세요!"

        st.session_state.messages.append({"role": "assistant", "content": reply})
        with st.chat_message("assistant"):
            st.write(reply)
