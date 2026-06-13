import streamlit as st
import pandas as pd

st.title("🎯 BoatPredictor")

with st.expander("🔍 レース選択と条件設定"):
    venue = st.selectbox("競艇場", ["桐生", "戸田", "江戸川", "平和島", "多摩川"])
    race = st.slider("レース番号", 1, 12, 1)
    wind = st.number_input("風速(m)", 0, 15, 2)
    submit = st.button("予想解析を実行")

if submit:
    st.divider()
    st.subheader(f"{venue} {race}R 予想")
    data = {"買い目": ["1-2-3", "1-3-2", "1-2-4"], "的中率": ["85%", "70%", "65%"]}
    df = pd.DataFrame(data)
    st.table(df)
    st.success("推奨度: 高")
