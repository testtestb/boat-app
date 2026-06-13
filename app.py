import streamlit as st
import random
import requests
from gtts import gTTS
import base64
import os

# 気象庁北九州アメダスID: 40111
STATION_ID = "40111"

# --- 関数定義 ---

# AIボイス（音声データ）を生成して自動再生する関数
def speak(text, filename="speech.mp3"):
    if not text: return
    # テキストを音声ファイルに変換
    tts = gTTS(text=text, lang='ja')
    tts.save(filename)
    
    # 自動再生用にHTML/HTML5オーディオを埋め込み
    with open(filename, "rb") as f:
        audio_bytes = f.read()
    st.audio(audio_bytes, format="audio/mp3", autoplay=True)

# アメダスデータを取得して天気情報を喋る
def get_and_speak_weather():
    try:
        # 最新データ取得
        time_url = "https://www.jma.go.jp/bosai/amedas/data/latest_time.txt"
        latest_time = requests.get(time_url).text.strip()
        data_url = f"https://www.jma.go.jp/bosai/amedas/data/map/{latest_time[:13]}0000.json"
        data = requests.get(data_url).json()
        station_data = data.get(STATION_ID)
        
        # 気圧取得
        pres = station_data.get("pres", [0])[0]
        
        # 判定と読み上げテキスト作成
        if pres < 1004.0:
            status_text = "【危険】気圧低下中です。雨の可能性が高いです。"
        elif pres < 1008.0:
            status_text = "【注意】天気が不安定です。ご注意ください。"
        else:
            status_text = "【安心】気象は安定しています。"
            
        weather_report = f"北九州の現在気圧は {pres} ヘクトパスカルです。{status_text}"
        return weather_report
    except:
        return "気象データの取得に失敗しました。"

# じゃんけんの判定
def play_janken(user_choice):
    choices = ["グー", "チョキ", "パー"]
    cpu_choice = random.choice(choices)
    
    if user_choice == cpu_choice:
        result = "あいこです。"
    elif (user_choice == "グー" and cpu_choice == "チョキ") or \
         (user_choice == "チョキ" and cpu_choice == "パー") or \
         (user_choice == "パー" and cpu_choice == "グー"):
        result = f"あなたの勝ちです！私は{cpu_choice}を出しました。"
    else:
        result = f"あなたの負けです…。私は{cpu_choice}を出しました。"
    
    return cpu_choice, result

# --- メイン画面 ---
st.set_page_config(page_title="音声先行監視 & じゃんけんAI", page_icon="📢")
st.title("📢 音声付き 先行監視 & じゃんけんAI")

# 1. 天気予報AIボイス
st.header("🌦️ 天気予報AIボイス")
if st.button("現在の天気を読み上げる"):
    with st.spinner('気象データを取得して音声を作成しています...'):
        report = get_and_speak_weather()
        st.write(report)
        speak(report, filename="weather.mp3")

st.write("---")

# 2. 音声じゃんけんAI
st.header("✊✌️🖐️ 音声じゃんけん")
user_hand = st.radio("手を選んでください", ["グー", "チョキ", "パー"])

if st.button("勝負！"):
    cpu_hand, result_text = play_janken(user_hand)
    
    col1, col2 = st.columns(2)
    col1.write(f"コンピュータ: **{cpu_hand}**")
    col2.write(f"結果: **{result_text}**")
    
    # じゃんけん結果のAI読み上げ
    janken_report = f"じゃんけん、{user_hand}。結果は、{result_text}"
    speak(janken_report, filename="janken.mp3")

st.caption("※音声の自動再生はブラウザの設定
