import streamlit as st
import pandas as pd

# 웹 페이지 제목 설정
st.title("🚗 목적지 도달 가능 여부 계산기")
st.write("거리와 속력을 입력하면 1시간 이내에 도착할 수 있는지 확인합니다.")

st.divider()

# 레이아웃을 두 개의 열로 나누어 입력란 배치
col1, col2 = st.columns(2)

with col1:
    # 거리 입력 (기본값 10.0, 최소값 0.0)
    d = st.number_input("거리 (km)", min_value=0.0, value=10.0, step=1.0)

with col2:
    # 속력 입력 (기본값 60.0, 최소값 0.1로 설정하여 0 나누기 오류 방지)
    s = st.number_input("속력 (km/h)", min_value=0.1, value=60.0, step=5.0)

st.divider()

# 핵심 로직 수행
if s > 0:
    time = d / s
    
    # 시간 결과 출력 (소수점 둘째 자리까지)
    st.subheader(
        f"⏱️ 예상 소요 시간: {time:.2f}시간 ({int(time * 60)}분)"
    )
    
    # 조건문 판단 및 출력
    if time <= 1:
        result = "갈 수 있다."
        st.success(f"🎉 결과: **{result}** (1시간 이내 도착 가능)")
    else:
        result = "갈 수 없다."
        st.error(f"⚠️ 결과: **{result}** (1시간 초과 소요)")
        
    # 기존 코드의 리스트 저장 및 출력 기능 구현 (데이터프레임 형태)
    results = [result]
    
    st.write("### 데이터 저장 결과 (리스트)")
    st.dataframe(pd.DataFrame({"판단 결과": results}))
else:
    st.warning("속력은 0보다 커야 합니다.")