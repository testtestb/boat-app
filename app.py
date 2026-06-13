import streamlit as st

st.title("🎯 BoatPredictor Pro [厳選勝負版]")

venues = [
    "桐生", "戸田", "江戸川", "平和島", "多摩川", "浜名湖", "蒲郡", "常滑", "津",
    "三国", "びわこ", "住之江", "尼崎", "鳴門", "丸亀", "児島", "宮島", "徳山",
    "下関", "若松", "芦屋", "福岡", "唐津", "大村"
]

venue = st.selectbox("競艇場を選択", venues)
tenji_1 = st.number_input("1号艇の展示タイム", 6.00, 8.00, 6.60, 0.01)
tenji_4 = st.number_input("4号艇の展示タイム", 6.00, 8.00, 6.60, 0.01)

# インが特に強い「稼げる場」リスト
gold_venues = ["大村", "芦屋", "徳山", "住之江"]

if st.button("的中重視で解析"):
    st.write("---")
    
    # 厳格な判定条件
    is_gold = venue in gold_venues
    is_stable = tenji_1 <= 6.55 and tenji_4 >= 6.70
    
    # ここがポイント：条件を満たさないレースは「予想しない」
    if is_gold and is_stable:
        st.success("【勝負レース】条件クリア！信頼度：高")
        st.write("推奨：1-2-3 / 1-2-4 / 1-3-2")
    elif not is_gold and is_stable:
        st.info("【中穴狙い】条件クリアですが慎重に")
        st.write("推奨：1-3-2 / 1-3-4")
    else:
        st.error("【見送り推奨】的中率が安定しません")
        st.write("今の条件では的中率が低いです。勝負を見送るのが賢明です。")
        st.write("※1号艇のタイムが6.55以下かつ、4号艇のタイムが6.70以上であるレースを狙ってください。")
