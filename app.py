import streamlit as st
import random
import requests
from gtts import gTTS
import os

# 気象庁北九州アメダスID: 40111
STATION_ID = "40111"

# AIボイス生成関数
def speak(text, filename="speech.mp3"):
    if not text: return
    tts = gTTS(text=text, lang='ja')
    tts.save(filename)
    with open(filename, "rb") as f:
        audio_bytes = f.read()
    st.audio(audio_bytes, format="audio/mp3", autoplay=True)

# 天気データ取得
def get_weather():
    try:
        time_url = "https://www.jma.go.jp/bosai/amedas/data/latest_time.txt"
        latest_time = requests.get(time_url).text.strip()
        data_url = f"https://www.jma.go.jp/bosai/amedas/data/map/{latest_time[:13]}0000.json"
        data = requests.get(data_url).json()
        station_data = data.get(STATION_ID)
        pres = station_data.get("pres", [0])[0]
        if pres < 1004.0:
            msg = f"北九州の現在気圧は{pres}ヘクトパスカル。雨の可能性が高いです。"
        else:
            msg = f"北九州の現在気圧は{pres}ヘクトパスカル。天気は安定しています。"
        return msg
    except:
        return "気象データの取得に失敗しました。"

# UI構築
st.title("📢 先行監視 & じゃんけんAI")

st.header("🌦️ 天気予報AI")
if st.button("天気を読み上げる"):
    msg = get_weather()
    st.write(msg)
    speak(msg)

st.header("✊✌️🖐️ じゃんけん")
hand = st.radio("手を選んでください", ["グー", "チョキ", "パー"])
if st.button("勝負！"):
    cpu = random.choice(["グー", "チョキ", "パー"])
    res = "あいこです。"
    if (hand=="グー" and cpu=="チョキ") or (hand=="チョキ" and cpu=="パー") or (hand=="パー" and cpu=="グー"):
        res = "あなたの勝ちです！"
    elif hand != cpu:
        res = "あなたの負けです。"
    st.write(f"コンピュータは{cpu}でした。{res}")
    speak(res)
