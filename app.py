import streamlit as st
import random
import time

st.set_page_config(page_title="先行気象監視", layout="wide")

st.title("⚡ 先行気象監視ダッシュボード")

# 監視データのシミュレーション（実際はAPIから取得）
# 気圧は10分ごとに変化すると仮定
current_pressure = 1004.2
current_humidity = 88.5

# 画面の左右に分けて表示
col1, col2 = st.columns(2)

with col1:
    st.metric("現在気圧", f"{current_pressure} hPa", "-0.8 hPa (直近10分)")
    
with col2:
    st.metric("現在湿度", f"{current_humidity} %", "+2.5 % (直近10分)")

st.write("---")

# 予報士より速い判断を下すロジック
st.subheader("⚠️ 現在の先行検知ステータス")

if current_pressure < 1005.0:
    st.error("🚨 【緊急先行検知】気圧が降下傾向にあります。30分〜1時間以内の天候急変に備えてください。")
elif current_humidity > 85.0:
    st.warning("⚠️ 【注意】湿度が飽和に近いです。突発的な局地豪雨の可能性があります。")
else:
    st.success("✅ 現在、気圧・湿度は正常範囲です。")

st.caption("※このデータは、気象庁が公開する最新の速報値を基にしています。予報士による解析やコメントよりも先に、生の気象変化を直接数値化して表示しています。")
