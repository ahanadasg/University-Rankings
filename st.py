# -*- coding: utf-8 -*-
"""st

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aItg1BKlQpFJXDaIsMdmqyQkDDUO_ecP
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt  # Import Matplotlib

# Sample university ranking data
data = {
    'University Name': [
        "Massachusetts Institute of Technology (MIT)",
        "University of Cambridge",
        "University of Oxford",
        "Harvard University",
        "Stanford University",
        "Imperial College London",
        "ETH Zurich",
        "National University of Singapore",
        "University College London",
        "University of California, Berkeley",
    ],
    '2024 Ranking': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    '2023 Ranking': [1, 2, 4, 5, 3, 6, 9, 11, 8, 27],
    'Location': [
        "United States",
        "United Kingdom",
        "United Kingdom",
        "United States",
        "United States",
        "United Kingdom",
        "Switzerland",
        "Singapore",
        "United Kingdom",
        "United States",
    ],
}

df = pd.DataFrame(data)

# Streamlit app
st.title("University Ranking Dashboard")

# Add a paragraph
st.write("Welcome to the University Ranking Dashboard. This dashboard provides insights into the rankings of top universities worldwide for the year 2023 and 2024.")


# Filter universities by location and year
st.sidebar.header("Filter Data")
location = st.sidebar.selectbox("Select Location", df['Location'].unique())
year = st.sidebar.selectbox("Select Year", ['2023', '2024'])

filtered_df = df[(df['Location'] == location) & (df[f'{year} Ranking'] > 0)]

# Create a bar chart for university ranking in the selected year using Plotly
fig = px.bar(filtered_df, x='University Name', y=f'{year} Ranking', title=f'University Rankings in {year}')
st.plotly_chart(fig)

# Create a bar chart for the distribution of university locations
location_counts = df['Location'].value_counts()
fig_bar_location = px.bar(x=location_counts.index, y=location_counts.values, title="Distribution of University Locations")
st.plotly_chart(fig_bar_location)

# Create a figure object for a bar chart using Matplotlib
fig_bar = plt.figure()
ax = fig_bar.add_subplot(111)
ax.bar(location_counts.index, location_counts.values)
ax.set_title("Distribution of University Locations (Matplotlib)")
ax.set_xlabel('Location')
ax.set_ylabel('Count')

# Save the bar chart as an image using Matplotlib
#fig_bar.savefig("university_locations_bar.png")  # Save the figure as an image file