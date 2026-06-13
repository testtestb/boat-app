import streamlit as st

st.title("🎯 BoatPredictor Pro")

# 日本全国の全24競艇場リスト
venues = [
    "桐生", "戸田", "江戸川", "平和島", "多摩川", "浜名湖", "蒲郡", "常滑", "津",
    "三国", "びわこ", "住之江", "尼崎", "鳴門", "丸亀", "児島", "宮島", "徳山",
    "下関", "若松", "芦屋", "福岡", "唐津", "大村"
]

venue = st.selectbox("競艇場を選択", venues)

# 展示タイム入力
st.subheader("直前情報入力")
tenji_time = st.number_input("1号艇の展示タイム (6.40〜6.80)", 6.40, 6.80, 6.60, 0.01)

if st.button("的中重視で解析"):
    st.write("---")
    
    # 競艇場ごとの特性（例：大村ならインが強いなど）を考慮した判定ロジック
    # インの強い場（大村・芦屋・徳山など）は基準を少し甘くする等の調整
    is_strong_venue = venue in ["大村", "芦屋", "徳山", "住之江"]
    
    if tenji_time < 6.55 or (is_strong_venue and tenji_time < 6.60):
        st.write("### ✅ イン鉄板レース")
        st.info("展示タイム良好。1号艇軸で勝負！")
        st.write("推奨買い目：1-23-234")
    elif tenji_time > 6.70:
        st.write("### ⚠️ 荒れる可能性あり")
        st.warning("1号艇の機力不足。センターからの捲りに警戒。")
        st.write("推奨買い目：3-14-145 / 4-13-135")
    else:
        st.write("### 💡 標準レース")
        st.write("推奨買い目：1-3-2 / 1-3-4")

    st.success(f"{venue}のデータと、展示タイム{tenji_time}を照合完了。")
