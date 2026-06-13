import streamlit as st
import pandas as pd
import numpy as np

st.title("📈 先行気象・時系列分析")

# 1. 過去の気圧変化（履歴）をシミュレーション
# 本来はDBやCSVに保存して蓄積します
data = {
    'time': ['12:30', '12:40', '12:50', '13:00', '13:10', '13:20', '13:30'],
    'pressure': [1005.2, 1004.8, 1004.5, 1004.2, 1004.0, 1003.8, 1003.5]
}
df = pd.DataFrame(data)

# 2. グラフの表示
st.subheader("気圧の推移（過去1時間）")
st.line_chart(df.set_index('time')['pressure'])

# 3. 傾き（変化の勢い）から予測を表示
st.write("### 予報解析")
slope = (df['pressure'].iloc[-1] - df['pressure'].iloc[-2])
if slope < 0:
    st.write(f"📉 **現在の傾向:** 10分ごとに {abs(slope):.1f} hPa 低下中。")
    st.write("→ **予測:** 気圧低下が止まらないため、今後30分〜1時間で天候がさらに悪化する可能性が高いです。")
else:
    st.write("📈 **現在の傾向:** 気圧は回復傾向です。")

st.info("※グラフが右肩下がりなら「悪化」、右肩上がりなら「回復」の合図です。")
