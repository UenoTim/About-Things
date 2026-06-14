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
levels = st.multiselect(
    "選擇車站等級",
    sorted(master["level"].unique()),
    default=sorted(master["level"].unique())
)
stop_options = st.multiselect(
    "是否停靠自強號",
    ["是", "否"],
    default=["是", "否"]
)
min_ridership = st.number_input(
    "最低年旅運量",
    min_value=0,
    value=0,
    step=100000
)
max_ridership = st.number_input(
    "最高年旅運量",
    min_value=0,
    value=int(master["annual_ridership"].max()),
    step=100000
)
filtered = master[
    (master["level"].isin(levels)) &
    (master["stop_text"].isin(stop_options)) &
    (master["annual_ridership"] >= min_ridership) &
    (master["annual_ridership"] <= max_ridership)
].sort_values("annual_ridership", ascending=False)
st.write(f"符合條件車站數：{len(filtered)}")
st.dataframe(
    filtered[
        ["staCode","station", "annual_ridership", "rank", "level", "stop_text"]
    ],hide_index=True
)