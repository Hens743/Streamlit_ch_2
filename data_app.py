import streamlit as st
import pandas as pd
import time

#App config
st.set_page_config(layout="centered")

#Data cache
@st.cache_data()
def load_data1(file_path1):
    default_data = pd.read_csv(file_path1)
    return default_data

@st.cache_data()
def load_data2(file_path2):
    uploaded_data = pd.read_csv(file_path2)
    return uploaded_data

@st.cache_resource()
def convert_df(df):
    return df.to_csv().encode('utf-8')

#Titles
st.header('Editable dataframes')
st.markdown ('Made with: Streamlit 1.20 - st.experimental_data_editor')

#Paths
file_path1 = "NYC_most_pop.csv"
file_path2 = st.file_uploader("Select CSV file to upload", type=["csv"])

#Drop box
option = st.selectbox('Select dataset',('Default dataset', 'Upload dataset'))
st.write('You selected:', option)

if option == 'Default dataset':
    data = load_data1(file_path1)
    st.experimental_data_editor(data, num_rows="dynamic")
    csv = convert_df(data)

if option == 'Upload dataset':
    if file_path2 is not None:
        data = load_data2(file_path2)
        st.experimental_data_editor(data, num_rows="dynamic")
        csv = convert_df(data)

#Download box
st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='Your_data.csv',
    mime='text/csv',
)
