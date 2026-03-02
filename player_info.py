import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


Batting_Bowling = pd.read_csv("Final_Batting_Bowling (1).csv")
Batting_Bowling.columns = Batting_Bowling.columns.str.strip()


team_option = st.selectbox("Select Team", sorted(Batting_Bowling['Final_Country'].dropna().unique()))


team_data = Batting_Bowling[Batting_Bowling['Final_Country'] == team_option]


player_option = st.selectbox("Select Player", sorted(team_data['name'].dropna().unique()))


player_data = team_data[team_data['name'] == player_option]


category = st.selectbox("Select Category", ["Batting","Bowling"])


if 'Categorey' in player_data.columns:
    player_data.rename(columns={'Categorey': 'Category'}, inplace=True)


category_data = player_data[player_data['Category'].str.lower() == category.lower()]


st.subheader(f"{player_option}'s {category} Stats")
st.write(category_data)


numeric_cols = ['Test', 'ODI', 'T20', 'IPL']


def clean_and_convert(val):
    if isinstance(val, str):
        if '/' in val or '-' in val or val.strip() in ['', '–', '-/-', 'nan']:
            return np.nan
    try:
        return float(val)
    except:
        return np.nan


if not category_data.empty:
    for i, (_, row) in enumerate(category_data.iterrows()):
        values = [clean_and_convert(row[col]) for col in numeric_cols]
        valid_data = [(col, v) for col, v in zip(numeric_cols, values) if not pd.isna(v)]

        if len(valid_data) == 0:
            continue  # Skip if no numeric data

        formats, clean_vals = zip(*valid_data)

        # --- 1. Bar Chart ---
        st.markdown("### 📊 Bar Chart")
        fig_bar, ax_bar = plt.subplots()
        ax_bar.bar(formats, clean_vals, color='steelblue')
        ax_bar.set_ylabel("Values")
        ax_bar.set_title(f"{player_option}'s {category} Stats")
        st.pyplot(fig_bar)

        # --- 2. Line Chart ---
        st.markdown("### 📈 Line Chart")
        fig_line, ax_line = plt.subplots()
        ax_line.plot(formats, clean_vals, marker='o', linestyle='--', color='green')
        ax_line.set_ylabel("Values")
        ax_line.set_title(f"{category} Trends for {player_option}")
        st.pyplot(fig_line)

        # --- 3. Pie Chart ---
        st.markdown("### 🥧 Pie Chart")
        fig_pie, ax_pie = plt.subplots()
        ax_pie.pie(clean_vals, labels=formats, autopct='%1.1f%%', startangle=90)
        ax_pie.set_title(f"{category} Contribution by Format")
        st.pyplot(fig_pie)

        break  # Show charts for just one valid row
else:
    st.warning(f"No {category} stats found for {player_option}.")

           