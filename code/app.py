import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image
import os
from projectHackworth2026.code.load import load_data, get_publisher_counts, get_average_stats, get_gender_distribution

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
        marvel_logo = Image.open(os.path.join("projectHackworth2026","code","cache", "marvel_logo.png"))
        st.image(marvel_logo, width=200)
    elif publisher == "DC Comics":
        dc_logo = Image.open(os.path.join("projectHackworth2026","code","cache", "dc_logo.png"))
        st.image(dc_logo, width=200)

# Define hex color mapping
publisher_colors = {
    "Marvel Comics": "#ED1D24",  # Marvel red
    "DC Comics": "#0072CE"       # DC blue
}

# Character count
st.header("Character Count by Publisher")
count_data = get_publisher_counts(df)
st.bar_chart(count_data)

# Average stats
st.header("Average Power Stats")
avg_stats = get_average_stats(df)
st.dataframe(avg_stats.round(2))

# Gender distribution
st.header("Gender Distribution")
gender_dist = get_gender_distribution(df).fillna(0)

# Ensure expected genders are present
expected_genders = ['Male', 'Female', '-']
for gender in expected_genders:
    if gender not in gender_dist.columns:
        gender_dist[gender] = 0

# Build traces manually
fig = go.Figure()
for gender in expected_genders:
    fig.add_trace(go.Bar(
        x=gender_dist.index,
        y=gender_dist[gender],
        name=gender,
        marker_color=[publisher_colors.get(pub, 'gray') for pub in gender_dist.index]
    ))

fig.update_layout(
    title="Gender Distribution by Publisher",
    barmode='group',
    xaxis_title="Publisher",
    yaxis_title="Character Count"
)

st.plotly_chart(fig, use_container_width=True)

# Top heroes per stat
st.header("Top Heroes by Power Stats")
stat_cols = ['intelligence', 'strength', 'speed', 'durability', 'power', 'combat']
for stat in stat_cols:
    st.subheader(f"Top 5 by {stat.title()}")
    top_heroes = df.sort_values(by=stat, ascending=False).head(5)
    fig = px.bar(
        top_heroes,
        x='name',
        y=stat,
        color='publisher',
        text=stat,
        color_discrete_map=publisher_colors
    )
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.caption("Data Source: https://akabab.github.io/superhero-api/")

