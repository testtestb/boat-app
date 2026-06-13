import streamlit as st
from PIL import Image

st.title("📸 ブラウザカメラアプリ")

# Streamlitのカメラ入力機能
picture = st.camera_input("写真を撮る")

if picture:
    st.image(picture)
    st.success("撮影完了！")
