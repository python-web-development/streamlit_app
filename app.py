import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Online Foods")
df = pd.read_csv("onlinefoods.csv")
st.write(df)

fig, ax = plt.subplots()
df.hist(
    bins=8,
    column="Age",
    grid=False,
    figsize=(8, 8),
    color="#86bf91",
    zorder=2,
    rwidth=0.9,
    ax=ax,
  )
st.write(fig)
