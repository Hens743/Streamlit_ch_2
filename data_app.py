import streamlit as st
import pandas as pd

df = pd.read_csv('NYC_most_pop.csv')
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")
edited_df = st.experimental_data_editor(df, num_rows="dynamic")

#favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]

