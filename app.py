import streamlit as st
import requests
import random

# 気象庁のデータから位置情報（北九州市）に基づく予言を生成
def get_weather_prophecy():
    try:
        # 気象庁の最新データ取得
        time_url = "https://www.jma.go.jp/bosai/amedas/data/latest_time.txt"
        latest_time = requests.get(time_url).text.strip()
        data_url = f"https://www.jma.go.jp/bosai/amedas/data/map/{latest_time[:13]}0000.json"
        data = requests.get(data_url).json()
        
        # 北九州市の観測所データ (40111)
        station_data = data.get("40111", {})
        pres = station_data.get("pres", [1013])[0]
        
        # 気圧に基づく予言ロジック
        if pres < 1008:
            return "雨の気配。今日は静かに内省の時間を持つと、新しいアイデアが降りてきます。", "☔"
        elif pres < 1015:
            return "空は移ろいやすい。心も柔軟に、変化を恐れず楽しんで。", "☁️"
        else:
            return "澄み渡る空があなたの背中を押しています。迷わず挑戦を。", "☀️"
    except:
        return "北九州の空の神託が届きません。もう一度占ってみましょう。", "🔮"

st.title("📍 北九州：天気予言の館")
st.write("今の北九州の空の状態から、あなたへのメッセージを読み解きます。")

if st.button("運命を占う"):
    with st.spinner('北九州の気象データを解析中...'):
        prophecy, icon = get_weather_prophecy()
        st.markdown(f"## {icon} 神託")
        st.write(f"### {prophecy}")
        st.balloons()

st.caption("※気象庁の北九州アメダス観測データを使用しています。")
