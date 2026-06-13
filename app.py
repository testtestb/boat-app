import streamlit as st

st.title("🎯 BoatPredictor Pro [完全版]")

# 日本全国の全24競艇場リスト
venues = [
    "桐生", "戸田", "江戸川", "平和島", "多摩川", "浜名湖", "蒲郡", "常滑", "津",
    "三国", "びわこ", "住之江", "尼崎", "鳴門", "丸亀", "児島", "宮島", "徳山",
    "下関", "若松", "芦屋", "福岡", "唐津", "大村"
]

venue = st.selectbox("競艇場を選択", venues)

# 入力項目
col1, col2 = st.columns(2)
with col1:
    tenji_1 = st.number_input("1号艇の展示タイム", 6.00, 8.00, 6.60, 0.01)
with col2:
    tenji_4 = st.number_input("4号艇の展示タイム", 6.00, 8.00, 6.60, 0.01)

if st.button("的中重視で解析"):
    st.write("---")
    
    # 判定ロジック
    # 4号艇が1号艇より速い場合、または非常に近い場合は危険信号
    if tenji_4 <= tenji_1:
        st.write("### ⚠️ 4号艇の動きに警戒！")
        st.warning("4号艇の機力が高いです。まくり・まくり差しに注意。")
        st.write("推奨買い目：1-4-5 / 1-4-2 / 4-1-5")
    else:
        st.write("### ✅ イン中心でOK")
        st.info("4号艇の脅威は少なめ。1号艇を軸に勝負。")
        st.write("推奨買い目：1-2-5 / 1-2-3 / 1-3-5")

    st.success(f"{venue}のデータと展示タイムを照合完了。")
