import streamlit as st

st.title("🎯 BoatPredictor Pro [的中重視版]")

# 設定
venues = ["桐生", "戸田", "江戸川", "平和島", "多摩川", "浜名湖", "蒲郡", "常滑", "津",
          "三国", "びわこ", "住之江", "尼崎", "鳴門", "丸亀", "児島", "宮島", "徳山",
          "下関", "若松", "芦屋", "福岡", "唐津", "大村"]

venue = st.selectbox("競艇場を選択", venues)

# 入力項目（信頼度を算出するための重要データ）
col1, col2 = st.columns(2)
with col1:
    rank = st.selectbox("1号艇の級別", ["A1", "A2", "B1", "B2"])
    wind = st.number_input("現在の風速(m)", 0, 15, 2)
with col2:
    tenji = st.number_input("1号艇の展示タイム", 6.00, 8.00, 6.60, 0.01)

if st.button("的中重視で解析"):
    # スコア計算（高いほど信頼度大）
    score = 0
    if rank == "A1": score += 40
    elif rank == "A2": score += 25
    if tenji < 6.65: score += 30
    if wind < 4: score += 30
    
    st.write("---")
    st.subheader(f"信頼度スコア: {score}/100")
    
    if score >= 80:
        st.success("【鉄板】自信を持って勝負できます！")
        st.write("推奨：1-23-2346")
    elif score >= 50:
        st.warning("【標準】的中は狙えますが、金額は控えめに。")
        st.write("推奨：1-3-24 / 1-2-3")
    else:
        st.error("【見送り推奨】荒れる要素が多すぎます。今回はパスしましょう。")
        st.write("※無理に買わず、次のレースを待つのが最も的中率を高める方法です。")
