import streamlit as st
import pandas as pd
import numpy as np

# 生成随机数据
dates = pd.date_range('2023-01-01', periods=30)
categories = ['Item A', 'Item B', 'Item C', 'Item D']
data = {
'date': np.random.choice(dates, 100),
'category': np.random.choice(categories, 100),
'value': np.random.randint(50, 500, 100)
}
df = pd.DataFrame(data)

# 加个标题
st.title('数据仪表盘')

# 显示总值
total_value = df['value'].sum()
st.metric(label='总收入', value=f'${total_value:,}')

# 时间趋势图
trend_data = df.groupby('date')['value'].sum()
st.subheader('时间趋势')
st.line_chart(trend_data)

# 分类排行
category_data = df.groupby('category')['value'].sum().sort_values(ascending=False)
st.subheader('类别排行')
st.bar_chart(category_data)

# 下拉框选类别
selected_category = st.selectbox('选择类别', categories)

# 筛选数据并画图
category_df = df[df['category'] == selected_category]
category_trend = category_df.groupby('date')['value'].sum()
st.subheader(f'{selected_category} 的趋势')
st.line_chart(category_trend)