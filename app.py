import streamlit as st
import pandas as pd

st.title("📋 オリジナル出走表作成ツール")

# 24場リスト
venues = [
    "桐生", "戸田", "江戸川", "平和島", "多摩川", "浜名湖", "蒲郡", "常滑", "津",
    "三国", "びわこ", "住之江", "尼崎", "鳴門", "丸亀", "児島", "宮島", "徳山",
    "下関", "若松", "芦屋", "福岡", "唐津", "大村"
]

venue = st.selectbox("開催地を選択", venues)
race_no = st.number_input("レース番号", 1, 12, 1)

st.write("---")
st.subheader("各艇のデータを入力")

# 6艇分のデータを格納するリスト
data = []
for i in range(1, 7):
    cols = st.columns(4)
    with cols[0]:
        st.write(f"**{i}号艇**")
    with cols[1]:
        rank = st.selectbox(f"{i}号艇 級別", ["A1", "A2", "B1", "B2"], key=f"r{i}")
    with cols[2]:
        motor = st.number_input(f"{i}号艇 モーター勝率", 0.0, 70.0, 40.0, 0.1, key=f"m{i}")
    with cols[3]:
        tenji = st.number_input(f"{i}号艇 展示タイム", 6.00, 7.50, 6.70, 0.01, key=f"t{i}")
    
    data.append({"艇番": i, "級別": rank, "モーター勝率": motor, "展示タイム": tenji})

if st.button("出走表を作成"):
    df = pd.DataFrame(data)
    st.write(f"### {venue} {race_no}R 出走表")
    st.table(df)
    st.success("表が完成しました。これをメモ代わりに活用してください。")
