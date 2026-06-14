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
col1, col2 = st.columns(2)
with col1:
    high_threshold = st.number_input(
        "高運量門檻",
        min_value=0,
        value=5000000,
        step=100000
    )
with col2:
    low_threshold = st.number_input(
        "低運量門檻",
        min_value=0,
        value=1000000,
        step=100000
    )
st.subheader("高運量不停靠站")
high_not_stop = master[
    (master["annual_ridership"] >= high_threshold)
    & (master["stop"] == 0)
].sort_values(
    by="staCode",
    ascending=True
)
st.dataframe(
    high_not_stop[
        [
            "staCode",
            "station",
            "annual_ridership",
            "rank",
            "level"
        ]
    ],
    hide_index=True
)
st.subheader("低運量停靠站")

low_stop = master[
    (master["annual_ridership"] <= low_threshold)
    & (master["stop"] == 1)
].sort_values(
    by="staCode",
    ascending=True
)
st.dataframe(
    low_stop[
        [
            "staCode",
            "station",
            "annual_ridership",
            "rank",
            "level"
        ]
    ],
    hide_index=True
)
col3, col4 = st.columns(2)
col3.metric(
    "高運量不停靠站數",
    len(high_not_stop)
)
col4.metric(
    "低運量停靠站數",
    len(low_stop)
)