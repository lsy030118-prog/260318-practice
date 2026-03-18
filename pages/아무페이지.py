import streamlit as st
from datetime import datetime

st.title("📝 일기장")

st.markdown("---")

# 날짜 선택
col1, col2 = st.columns(2)
with col1:
    diary_date = st.date_input("날짜", value=datetime.now())
with col2:
    mood = st.selectbox("오늘의 기분", ["😊 기쁨", "😔 슬픔", "😤 화남", "😴 피로", "😌 평온", "😍 행복", "😟 불안"])

st.markdown("---")

# 제목
st.subheader("제목")
title = st.text_input("제목을 입력해주세요.", placeholder="예: 오늘 하루")

# 내용
st.subheader("내용")
content = st.text_area("내용을 입력해주세요.", height=200, placeholder="오늘 9시 30분 셔틀을 타고 학교에 왔다. 계란과 아이스티를 먹으며 교생 사전교육을 들었다. 그리고 지금 수논논 수업을 하고 있다.")

st.markdown("---")

# 저장 버튼
if st.button("저장"):
    if title and content:
        st.success(f"✅ {diary_date.strftime('%Y년 %m월 %d일')} 일기가 저장되었습니다!")
        st.info(f"제목: {title}\n\n기분: {mood}")
    else:
        st.error("제목과 내용을 모두 작성해주세요.")

