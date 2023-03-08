import streamlit as st
import pandas as pd

st.set_page_config(layout="centered")

@st.cache_data()
def load_data(file_path):
    df = pd.read_csv(file_path)
    return df
  
st.header('Dataframes editor app')
st.markdown ('Streamlit 1.19 - st.experimental_data_editor')

file_path = st.file_uploader("Select CSV file to upload", type=["csv"])

edited_df = st.experimental_data_editor(df, num_rows="dynamic")

favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")

