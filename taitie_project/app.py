import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="台鐵分析系統",
    page_icon="🚆",
    layout="wide"
)

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

st.title("台鐵旅運量與自強號停站分析_以民國113年為例")
st.header("")
st.header("請從左側選單選擇功能")
st.header("")

master = pd.read_excel(
    "data/master_table.xlsx"
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "車站總數",
        len(master)
    )

with col2:
    st.metric(
        "停靠站數",
        len(master[master["stop"] == 1])
    )

with col3:
    st.metric(
        "不停靠站數",
        len(master[master["stop"] == 0])
    )