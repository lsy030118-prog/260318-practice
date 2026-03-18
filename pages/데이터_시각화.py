import streamlit as st
import pandas as pd
import numpy as np

st.title("데이터 시각화")

# 샘플 데이터: 월별 판매량
st.subheader("월별 판매량 막대 그래프")
data_sales = {
    '월': ['1월', '2월', '3월', '4월', '5월', '6월'],
    '판매량': [100, 120, 150, 130, 170, 200]
}
df_sales = pd.DataFrame(data_sales)
df_sales.set_index('월', inplace=True)
st.bar_chart(df_sales)

# 선 그래프
st.subheader("시간에 따른 데이터 선 그래프")
x = np.linspace(0, 10, 100)
y = np.sin(x)
df_line = pd.DataFrame({
    '시간': x,
    '값': y
})
df_line.set_index('시간', inplace=True)
st.line_chart(df_line)

# 산점도
st.subheader("두 변수의 관계 산점도")
x_scatter = np.random.randn(100)
y_scatter = 2 * x_scatter + np.random.randn(100)
df_scatter = pd.DataFrame({
    '변수 X': x_scatter,
    '변수 Y': y_scatter
})
st.scatter_chart(df_scatter)

# 테이블 표시
st.subheader("판매 데이터 테이블")
table_data = {
    '월': ['1월', '2월', '3월', '4월', '5월', '6월'],
    '판매량': [100, 120, 150, 130, 170, 200],
    '성장률': ['0%', '+20%', '+25%', '-13%', '+31%', '+18%']
}
df_table = pd.DataFrame(table_data)
st.table(df_table)
