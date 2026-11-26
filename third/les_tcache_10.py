import streamlit as st

st.title("계산 결과 재사용")

@st.cache_data(ttl=60)
def sum_squares(limit):
    # 함수의 계산 결과를 캐시에 저장
    # ttl=60은 저장한 캐시를 60초 동안 유지한다는 의미
    return sum(n * n for n in range(limit + 1))
    # 0부터 limit까지 각 숫자를 제곱해서 모두 더함
    #limit 숫자가 5라면 
    #0*0 + 1*1 + 2*2 + 3*3 + 4*4 + 5*5 = 55
    #그런데 range는 마지막 숫자를 포함하지 않기때문 1을 더 더해줌


limit = st.number_input("마지막 숫자 제곱", min_value=1, max_value=10000, value=3)

with st.spinner("계산중"):
    # 계산하는 동안 로딩 메시지 표시
    result = sum_squares(int(limit))
    # 입력받은 숫자를 정수로 변환하고 함수 실행

st.metric("제곱함", result)
# 계산 결과를 화면에 출력

if st.button("이 함수 캐시 지우기"):
    # 캐시 삭제 버튼 생성
    
    sum_squares.clear()
     # sum_squares 함수에 저장된 캐시 삭제
    st.success("이 캐시를 지웟습니다")



#캐시는 한 번 계산한 결과를 저장해 두었다가, 
#같은 조건으로 다시 계산할 때 빠르게 
# 결과를 가져오는 기능