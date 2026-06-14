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
options = {
    f"{row['staCode']}＿{row['station']}": row["staCode"]
    for _, row in master.sort_values("staCode").iterrows()
}

selected = st.multiselect(
    "請選擇要比較的車站",
    options.keys()
)

if selected:
    selected_codes = [options[item] for item in selected]

    compare = master[
        master["staCode"].isin(selected_codes)
    ].sort_values(
        by="staCode",
        ascending=True
    )

    st.subheader("各車站運量資料")

    st.dataframe(
        compare[
            [
                "staCode",
                "station",
                "annual_ridership",
                "rank",
                "level",
                "stop_text"
            ]
        ],
        use_container_width=True,
        hide_index=True
    )

    st.subheader("各車站運量比較圖")

    fig, ax = plt.subplots(figsize=(8, 4))

    ax.bar(
        compare["station"],
        compare["annual_ridership"]
    )

    ax.set_ylabel("年旅運量")
    ax.set_xlabel("車站")
    ax.set_title("自選車站年旅運量比較")

    plt.xticks(rotation=45)

    st.pyplot(fig)