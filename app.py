import streamlit as st
import streamlit.components.v1 as components

st.title("📍 天気信号機 - 現在地監視")

# ブラウザから位置情報を取得するJS
js_code = """
<script>
    navigator.geolocation.getCurrentPosition(
        (position) => {
            const lat = position.coords.latitude;
            const lon = position.coords.longitude;
            // 実際はここで値をStreamlitに送る処理を実装
            document.write("現在地を特定中...");
        }
    );
</script>
"""
components.html(js_code, height=50)

# シミュレーション：本来はAPIから取得した気圧・湿度
pressure = 1003.5 
humidity = 87.0

st.write("---")
st.subheader("今の空模様の状態")

# 信号機ロジック
if pressure < 1004.0:
    st.error("🔴 今すぐ傘が必要です！")
    st.write("気圧がかなり下がっています。まもなく雨が降るか、現在降っている可能性が高いです。")
elif pressure < 1008.0:
    st.warning("🟡 天気が変わりやすいです！")
    st.write("気圧が少し不安定です。空が暗くなったら雨の合図です。")
else:
    st.success("🟢 現在は安定しています。")
    st.write("当面の間は天気が崩れる心配は低そうです。")

st.info("※ブラウザの「位置情報の許可」をONにしてください。自動で今いる場所の天気を判定します。")
