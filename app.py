import streamlit as st

st.title("🎯 BoatPredictor [敗因分析強化版]")

# 入力項目
col1, col2 = st.columns(2)
with col1:
    venue = st.selectbox("競艇場", ["大村", "芦屋", "徳山", "住之江", "戸田", "その他"])
    tenji_1 = st.number_input("1号艇展示", 6.00, 8.00, 6.60, 0.01)
with col2:
    tenji_4 = st.number_input("4号艇展示", 6.00, 8.00, 6.60, 0.01)

if st.button("的中重視で解析"):
    st.write("---")
    # 4号艇の展示が1号艇より速い場合、波乱のサイン
    if tenji_4 < tenji_1:
        st.write("### ⚠️ 4号艇の動きに警戒！")
        st.warning("4号艇の展示が好調です。1-4の筋を買い目に加えるべきでした。")
        st.write("推奨買い目：1-4-5 / 1-4-2 / 1-4-3")
    else:
        st.write("### ✅ 1号艇中心でOK")
        st.info("4号艇の脅威は少なそう。本命で勝負。")
        st.write("推奨買い目：1-2-3 / 1-2-5 / 1-3-5")
