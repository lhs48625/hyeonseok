import streamlit as st

with st.form("order_form"):
    name = st.text_input("이름")
    raw = st.text_input("수량", value="1")
    submitted = st.form_submit_button("계산")
if submitted:
    # 계산 버튼을 눌렀을 때 실행

    st.session_state.pop("result", None)
     # 기존에 저장된 결과가 있다면 삭제

    try:
        quantity = int(raw)
        # 입력받은 수량을 문자열에서 정수형으로 변환

        if not name.strip() or not 1 <= quantity <= 100:
            raise ValueError("이름과 수량 범위 확인")
         # 이름이 비어 있거나 수량이 1~100 범위가 아니면 오류 발생
        
        st.session_state.result = quantity * 8000
          # 수량에 8000원을 곱해 총액 계산 후 세션 상태에 저장

    except ValueError:
        # 정수 변환이나 입력값 검증에서 오류가 발생하면 실행

        st.error("입력한 이름과 수량을 확인")
        # 오류 메시지 출

if "result" in st.session_state:
    # 세션 상태에 result 값이 저장되어 있는지 확인

    st.metric("총액", f"{st.session_state.result:,}원")
    # 계산된 총액을 콤마(,)를 포함한 원화 형식으로 화면에 출력