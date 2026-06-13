import streamlit as st

st.title("🎯 BoatPredictor Pro [的中＆資金管理]")

# 競艇場リスト（イン逃げ率を考慮した重み付け）
venue_weight = {
    "大村": 1.2, "芦屋": 1.2, "徳山": 1.1, "住之江": 1.1, "戸田": 0.8, "江戸川": 0.8
}
venues = ["桐生", "戸田", "江戸川", "平和島", "多摩川", "浜名湖", "蒲郡", "常滑", "津",
          "三国", "びわこ", "住之江", "尼崎", "鳴門", "丸亀", "児島", "宮島", "徳山",
          "下関", "若松", "芦屋", "福岡", "唐津", "大村"]

venue = st.selectbox("競艇場を選択", venues)
rank = st.selectbox("1号艇の級別", ["A1", "A2", "B1", "B2"])
tenji = st.number_input("1号艇の展示タイム", 6.00, 8.00, 6.60, 0.01)
wind = st.number_input("風速(m)", 0, 15, 2)

if st.button("的中重視で解析"):
    # スコア計算（場×級別×展示×風速）
    score = (venue_weight.get(venue, 1.0) * 20)
    if rank == "A1": score += 40
    elif rank == "A2": score += 20
    if tenji < 6.60: score += 30
    if wind < 4: score += 20
    
    st.write("---")
    st.subheader(f"勝負度スコア: {min(score, 100):.0f}/100")
    
    if score >= 80:
        st.success("【勝負レース】的中確率が高いです。")
        st.write("推奨買い目：1-23-234（資金配分: 本命60% 対抗40%）")
    elif score >= 60:
        st.info("【様子見レース】的中は狙えます。")
        st.write("推奨買い目：1-2-3 / 1-3-2（少額で投資）")
    else:
        st.error("【見送り推奨】的中確率が低いです。ここは我慢の時です。")
        st.write("※プロは「当たらないレースで買わない」ことで資金を守ります。")
