import streamlit as st
import pandas as pd

st.set_page_config(layout="centered")


@st.cache_data()
def load_data(file_path):
    df = pd.read_csv(file_path)
    return df
  
st.header('Editable dataframes app with st.experimental_data_editor (Streamlit 1.19)')
file_path = st.file_uploader("Select CSV file to upload", type=["csv"])
st.experimental_data_editor(df, num_rows="dynamic")

#favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]

