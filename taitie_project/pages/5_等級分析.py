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
st.subheader("各等級平均年旅運量")
level_avg = (
    master
    .groupby(["level", "level_score"])["annual_ridership"]
    .mean()
    .reset_index()
    .sort_values(
        by="level_score",
        ascending=True
    )
)
level_avg["annual_ridership"] = (
    level_avg["annual_ridership"]
    .round(0)
    .astype(int)
)
st.dataframe(level_avg,hide_index=True)
fig, ax = plt.subplots(figsize=(8,4))
ax.bar(
    level_avg["level"],
    level_avg["annual_ridership"]
)
ax.set_title("各等級平均年旅運量")
ax.set_xlabel("車站等級")
ax.set_ylabel("平均年旅運量")
st.pyplot(fig)
st.subheader("停靠站與未停靠站平均運量比較")
stop_avg = master.groupby("stop_text")["annual_ridership"].mean().reset_index()
stop_avg["annual_ridership"] = (
    stop_avg["annual_ridership"]
    .round(0)
    .astype(int)
)
st.dataframe(stop_avg,hide_index=True)
fig, ax = plt.subplots(figsize=(6,4))
ax.bar(stop_avg["stop_text"], stop_avg["annual_ridership"])
ax.set_title("停靠與未停靠平均年旅運量")
ax.set_xlabel("是否停靠自強號")
ax.set_ylabel("平均年旅運量")
st.pyplot(fig)