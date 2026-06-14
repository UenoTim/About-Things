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
total_stations = len(master)
stop_count = len(master[master["stop"] == 1])
no_stop_count = len(master[master["stop"] == 0])
col1, col2, col3 = st.columns(3)
col1.metric("車站總數", total_stations)
col2.metric("自強號停靠站", stop_count)
col3.metric("未停靠站", no_stop_count)
st.subheader("民國113年Top20旅運量車站")
top20 = master.sort_values(
    by="annual_ridership",
    ascending=False
).head(20)
st.dataframe(
    top20[["rank","staCode","station", "annual_ridership", "level", "stop_text"]],
    hide_index=True
)
fig, ax = plt.subplots(figsize=(10, 5))
ax.bar(
    top20["station"],
    top20["annual_ridership"]
)
ax.set_title("Top20 年旅運量車站")
ax.set_xlabel("車站")
ax.set_ylabel("年旅運量")
plt.xticks(rotation=45)
st.pyplot(fig)