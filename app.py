import streamlit as st

st.title("🎵 My Web Music Player")

# 曲のリスト（好きな曲のURLをここに入れる）
music_url = "https://example.com/your-song.mp3"

st.subheader("今聴いている曲")
st.audio(music_url, format="audio/mp3")

if st.button("次の曲へ"):
    st.write("曲を切り替えています...")
