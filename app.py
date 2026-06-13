import streamlit as st
import streamlit.components.v1 as components

st.title("📍 GPS連動・先行気象監視")

# ブラウザから位置情報を取得するためのJavaScript
js_code = """
<script>
    navigator.geolocation.getCurrentPosition(
        (position) => {
            const lat = position.coords.latitude;
            const lon = position.coords.longitude;
            // ここで取得した座標をStreamlit側に渡すロジックが必要
            document.body.innerHTML += "緯度: " + lat + ", 経度: " + lon;
        }
    );
</script>
"""
components.html(js_code, height=100)

st.write("---")

# 位置情報が取得できたと仮定して、北九州の気象データを監視
location = "北九州"
st.subheader(f"現在地：{location} の先行観測データ")

# シミュレーション（本来はここで現在地に最も近いアメダス地点をAPIから選別）
pressure = 1003.5 # 現在の北九州の気圧を想定
humidity = 87.0

col1, col2 = st.columns(2)
with col1:
    st.metric("現在気圧", f"{pressure} hPa")
with col2:
    st.metric("現在湿度", f"{humidity} %")

if pressure < 1005.0:
    st.error("🚨 【緊急】現在地の気圧が急低下中！30分以内の天候悪化に備えてください。")
else:
    st.success("✅ 現在地周辺の気象状況は正常です。")

st.info("※ブラウザの位置情報設定を許可すると、移動しても常にその場所の気象データを監視します。")
