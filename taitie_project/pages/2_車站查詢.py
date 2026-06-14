import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

st.markdown("""
<style>
.stApp {
    background-color: #f7f9fb;
}

.block-container {
    padding-top: 4rem;
}

h1 {
    color: #1f4e79;
    font-size: 42px;
    line-height: 1.4;
}

h2, h3 {
    color: #1f4e79;
}
</style>
""", unsafe_allow_html=True)

matplotlib.rcParams["font.family"] = "Arial Unicode MS"
matplotlib.rcParams["axes.unicode_minus"] = False
master = pd.read_excel("data/master_table.xlsx")
master["percentile"] = (
    master["annual_ridership"].rank(pct=True) * 100
)
options = {
    f"{row['staCode']}＿{row['station']}": row['staCode']
    for _, row in master.sort_values("staCode").iterrows()
}
selected = st.selectbox(
    "請選擇車站",
    options.keys()
)
result = master[
    master["staCode"] == options[selected]
].iloc[0]

st.subheader(
    f'{result["staCode"]}｜{result["station"]}'
)
st.write("車站代碼：", result["staCode"])
st.write("車站等級：", result["level"])
st.write("是否停靠自強號：", result["stop_text"])
st.write("年旅運量：", f'{result["annual_ridership"]:,}')
st.write("日均運量：", f'{result["avg_daily"]:,.0f}')
st.write("運量排名：", int(result["rank"]))
st.write(
    "運量百分位：",
    f'{result["percentile"]:.1f}%'
)