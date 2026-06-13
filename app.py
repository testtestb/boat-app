import streamlit as st

st.title("🎯 BoatPredictor Pro [プロ分析モデル]")

# 各場のイン逃げ信頼度（2026年時点の統計的傾向を反映）
venue_stats = {
    "大村": 0.72, "芦屋": 0.68, "徳山": 0.65, "住之江": 0.62, "戸田": 0.45, "江戸川": 0.48
}

venues = ["桐生", "戸田", "江戸川", "平和島", "多摩川", "浜名湖", "蒲郡", "常滑", "津",
          "三国", "びわこ", "住之江", "尼崎", "鳴門", "丸亀", "児島", "宮島", "徳山",
          "下関", "若松", "芦屋", "福岡", "唐津", "大村"]

# プロの入力項目
venue = st.selectbox("競艇場を選択", venues)
is_a1 = st.checkbox("1号艇はA1級選手ですか？")
tenji_1 = st.number_input("1号艇の展示タイム", 6.00, 8.00, 6.60, 0.01)
wind = st.number_input("風速(m)", 0.0, 15.0, 2.0)

if st.button("プロモデルで解析"):
    # 確率計算ロジック
    base_rate = venue_stats.get(venue, 0.55) # その場の平均イン逃げ率
    
    # 補正計算
    if is_a1: base_rate += 0.15
    if tenji_1 < 6.55: base_rate += 0.10
    if wind > 5.0: base_rate -= 0.20 # 強い向かい風はインが飛ぶ
    
    # 最終的中確率
    final_rate = min(base_rate, 0.95)
    
    st.write("---")
    st.subheader(f"勝率予想: {final_rate:.1%}")
    
    if final_rate > 0.70:
        st.success("【プロ推奨：本命】このレースは投資価値あり。")
        st.write("推奨：1-23-234")
    elif final_rate > 0.50:
        st.info("【プロ推奨：様子見】展開次第では的中。")
        st.write("推奨：1-2-3 / 1-3-2")
    else:
        st.error("【プロ推奨：見送り】的中期待値が低すぎます。")
        st.write("※無理に賭けるレースではありません。")
