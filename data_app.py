import streamlit as st
import pandas as pd


@st.cache_data()
def load_data(file_path):
    df = pd.read_csv(file_path)
    return df
  
st.header('Editable dataframes with st.experimental_data_editor (Streamlit 1.19)')

edited_df = st.experimental_data_editor(df, num_rows="dynamic")

#favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]

