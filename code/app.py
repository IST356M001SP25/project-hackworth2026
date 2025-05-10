import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image
import os
from load import load_data, get_publisher_counts, get_average_stats, get_gender_distribution

st.set_page_config(layout="wide")
st.title("Marvel vs DC: Superhero Stats Dashboard")

# Load data
df = load_data()

# Sidebar filters
st.sidebar.header("Filters")
publisher = st.sidebar.selectbox("Choose Publisher", ["All", "Marvel Comics", "DC Comics"])
if publisher != "All":
    df = df[df['publisher'] == publisher]

# Show logos
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if publisher == "Marvel Comics":
        marvel_logo = Image.open(os.path.join("cache", "marvel_logo.png"))
        st.image(marvel_logo, width=200)
    elif publisher == "DC Comics":
        dc_logo = Image.open(os.path.join("cache", "dc_logo.png"))
        st.image(dc_logo, width=200)

# Character count
st.header("Character Count by Publisher")
count_data = get_publisher_counts(load_data())
st.bar_chart(count_data)

# Average stats
st.header("Average Power Stats")
avg_stats = get_average_stats(load_data())
st.dataframe(avg_stats.round(2))

# Gender distribution
st.header("Gender Distribution")
gender_dist = get_gender_distribution(load_data()).reset_index()
fig = px.bar(gender_dist, x='publisher', y=['Male', 'Female', '-'], title="Gender Distribution")
st.plotly_chart(fig, use_container_width=True)

# Top heroes per stat
st.header("Top Heroes by Power Stats")
stat_cols = ['intelligence', 'strength', 'speed', 'durability', 'power', 'combat']
for stat in stat_cols:
    st.subheader(f"Top 5 by {stat.title()}")
    top_heroes = df.sort_values(by=stat, ascending=False).head(5)
    fig = px.bar(top_heroes, x='name', y=stat, color='publisher', text=stat)
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.caption("Data Source: https://akabab.github.io/superhero-api/")
