import streamlit as st

st.title("🎯 BoatPredictor AI [出走表分析モデル]")

# 場ごとのイン逃げ指数 (1.0が平均、高いほどインが強い)
venue_bias = {
    "大村": 1.4, "芦屋": 1.3, "徳山": 1.3, "住之江": 1.2, "尼崎": 1.2,
    "戸田": 0.7, "江戸川": 0.7, "平和島": 0.8, "多摩川": 0.9,
    "その他": 1.0
}

# 競艇場リスト
venues = ["桐生", "戸田", "江戸川", "平和島", "多摩川", "浜名湖", "蒲郡", "常滑", "津",
          "三国", "びわこ", "住之江", "尼崎", "鳴門", "丸亀", "児島", "宮島", "徳山",
          "下関", "若松", "芦屋", "福岡", "唐津", "大村"]

# --- 入力インターフェース ---
venue = st.selectbox("開催地を選択", venues)
st.subheader("出走表データの入力")
rank_1 = st.selectbox("1号艇の級別", ["A1", "A2", "B1", "B2"])
motor_1 = st.number_input("1号艇のモーター勝率 (%)", 0.0, 70.0, 45.0, 0.1)
tenji_1 = st.number_input("1号艇の展示タイム", 6.00, 7.00, 6.60, 0.01)

if st.button("的中重視で解析"):
    st.write("---")
    
    # 1. 競艇場補正の取得
    bias = venue_bias.get(venue, venue_bias["その他"])
    
    # 2. 級別スコア計算
    rank_score = {"A1": 30, "A2": 20, "B1": 10, "B2": 0}.get(rank_1, 0)
    
    # 3. モーター・タイム総合評価
    # タイムが6.60以下なら高評価、モーター勝率も加味
    time_score = max(0, (6.70 - tenji_1) * 200)
    motor_score = motor_1 / 2
    
    # 総合スコア（場ごとのバイアスを掛ける）
    total_score = (rank_score + time_score + motor_score) * bias
    
    # --- 結果の出力 ---
    st.write(f"### 解析スコア: {total_score:.1f}")
    
    if total_score > 60:
        st.success("【本命】イン逃げ濃厚。信頼度が高いです。")
        st.write("推奨：1-23-234 / 1-2-5")
    elif total_score > 45:
        st.info("【狙い目】1号艇中心ですが、ヒモ荒れに注意。")
        st.write("推奨：1-3-2 / 1-2-4 / 3-1-2")
    else:
        st.warning("【注意】インが苦戦する可能性あり。")
        st.write("推奨：3-1-2 / 3-4-1 / 4-1-3")

    st.caption(f"{venue}の特性（補正値:{bias}）を考慮した予想です。")
