import streamlit as st
import pandas as pd
import plotly.express as px
from projectHackworth2026.code.load import load_data, get_publisher_counts, get_average_stats, get_gender_distribution

st.set_page_config(layout="wide")
st.title("Marvel vs DC: Superhero Stats Dashboard")

df = load_data()

st.sidebar.header("Filters")
publisher = st.sidebar.selectbox("Choose Publisher", ["All", "Marvel Comics", "DC Comics"])
if publisher != "All":
    df = df[df['publisher'] == publisher]

st.header("Character Count by Publisher")
count_data = get_publisher_counts(load_data())
st.bar_chart(count_data)

st.header("Average Power Stats")
avg_stats = get_average_stats(load_data())
st.dataframe(avg_stats.round(2))

st.header("Gender Distribution")
gender_dist = get_gender_distribution(load_data()).reset_index()
fig = px.bar(gender_dist, x='publisher', y=['Male', 'Female', '-'], title="Gender Distribution")
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.caption("Data Source: https://akabab.github.io/superhero-api/")
