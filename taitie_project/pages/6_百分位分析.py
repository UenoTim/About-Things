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

options_p = {
    f"{row['staCode']}＿{row['station']}": row["staCode"]
    for _, row in master.sort_values("staCode").iterrows()
}

selected_p = st.selectbox(
    "選擇要分析百分位的車站",
    options_p.keys(),
    key="percentile_station"
)

row = master[
    master["staCode"] == options_p[selected_p]
].iloc[0]

st.metric(
    "運量百分位",
    f"{row['percentile']:.1f}%"
)

st.write(
    f"{row['station']}站的年旅運量超過全體約 {row['percentile']:.1f}% 的車站。"
)