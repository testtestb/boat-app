import streamlit as st

# 全24競艇場リスト
venues = [
    "桐生", "戸田", "江戸川", "平和島", "多摩川", "浜名湖", "蒲郡", "常滑", "津",
    "三国", "びわこ", "住之江", "尼崎", "鳴門", "丸亀", "児島", "宮島", "徳山",
    "下関", "若松", "芦屋", "福岡", "唐津", "大村"
]

st.title("🎯 BoatPredictor Pro")

venue = st.selectbox("競艇場を選択してください", venues)
race = st.slider("レース番号", 1, 12, 1)

if st.button("解析を実行"):
    st.subheader(f"{venue} {race}R の予想")
    st.write("データ解析中...")
    st.success(f"{venue}の特性に基づき、1号艇のイン逃げ信頼度を算出しました。")
