import streamlit as st
import pandas as pd

#App config
st.set_page_config(layout="centered")

#Paths
file_path1 = pd.read_csv("NYC_most_pop.csv")
file_path2 = st.file_uploader("Select CSV file to upload", type=["csv"])

#Data cache
@st.cache_data()
def load_data(file_path1):
    default_data = pd.read_csv(file_path1)
    return default_data

@st.cache_data()
def load_data(file_path2):
    uploaded_data = pd.read_csv(file_path2)
    return uploaded_data

#Titles
st.header('Dataframes editor app')
st.markdown ('Made with: Streamlit 1.19 - st.experimental_data_editor')

#Drop box
option = st.selectbox('Select dataset',('Default dataset', 'Upload dataset'))
st.write('You selected:', option)

if option == 'Upload dataset':
    st.file_uploader("Select CSV file to upload", type=["csv"])

#Editable dataset
df= [default_data,uploaded_data]
st.experimental_data_editor(df, num_rows="dynamic")

#favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
#st.markdown(f"Your favorite command is **{favorite_command}** 🎈")
