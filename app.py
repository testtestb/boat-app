import streamlit as st
import requests

# 気象庁のアメダスデータ（北九州観測所ID: 40111）
STATION_ID = "40111"

@st.cache_data(ttl=600) # 10分ごとにデータを更新
def get_amedas_data():
    try:
        # 最新のデータ時刻を取得
        time_url = "https://www.jma.go.jp/bosai/amedas/data/latest_time.txt"
        latest_time = requests.get(time_url).text.strip()
        
        # 観測データURL
        data_url = f"https://www.jma.go.jp/bosai/amedas/data/map/{latest_time[:13]}0000.json"
        data = requests.get(data_url).json()
        
        return data.get(STATION_ID)
    except Exception as e:
        return None

st.set_page_config(page_title="北九州・正確な気象監視", page_icon="📍")
st.title("📍 北九州：リアルタイム気象監視")

# データ取得
data = get_amedas_data()

if data:
    # 気圧(hPa)と湿度(%)を取得
    # [0] はその観測点の現在値を指します
    pres = data.get("pres", [0])[0]
    humid = data.get("humid", [0])[0]
    
    col1, col2 = st.columns(2)
    col1.metric("現在気圧", f"{pres} hPa")
    col2.metric("現在湿度", f"{humid} %")
    
    st.write("---")
    
    # 信号機ロジックによる直感判定
    if pres < 1004.0:
        st.error("🔴 【危険】気圧低下中！雨雲が接近中です。")
    elif pres < 1008.0:
        st.warning("🟡 【注意】天気が不安定です。空の変化に注意してください。")
    else:
        st.success("🟢 【安心】気象は安定しています。")
else:
    st.error("データ取得に失敗しました。")

st.caption("※気象庁のアメダス観測所から取得したリアルタイム実測値です。")
