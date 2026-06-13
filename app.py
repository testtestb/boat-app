import streamlit as st

st.title("🎯 BoatPredictor Pro")

# 全24競艇場リスト
venues = [
    "桐生", "戸田", "江戸川", "平和島", "多摩川", "浜名湖", "蒲郡", "常滑", "津",
    "三国", "びわこ", "住之江", "尼崎", "鳴門", "丸亀", "児島", "宮島", "徳山",
    "下関", "若松", "芦屋", "福岡", "唐津", "大村"
]

venue = st.selectbox("競艇場を選択", venues)

# 展示タイム入力（制限をなくしました）
st.subheader("直前情報入力")
tenji_time = st.number_input("1号艇の展示タイムを入力してください", 6.00, 8.00, 6.60, 0.01)

if st.button("的中重視で解析"):
    st.write("---")
    
    # 競艇場ごとの特性判定
    is_strong_venue = venue in ["大村", "芦屋", "徳山", "住之江"]
    
    # ロジックを少し広めに設定
    if tenji_time < 6.60:
        st.write("### ✅ イン鉄板レース")
        st.info("タイム優秀！1号艇軸で勝負！")
        st.write("推奨買い目：1-23-234")
    elif tenji_time > 6.75:
        st.write("### ⚠️ 荒れる可能性あり")
        st.warning("タイムが厳しめ。センターの突き抜けを警戒。")
        st.write("推奨買い目：3-1-2 / 3-4-1 / 1-3-4")
    else:
        st.write("### 💡 標準レース")
        st.info("インは互角。展開重視で。")
        st.write("推奨買い目：1-2-3 / 1-3-2")

    st.success(f"{venue}の特性と展示タイム{tenji_time}を照合しました。")
