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

#Titles
st.header('Dataframes editor Web App')
st.markdown ('Made with: Streamlit 1.19 - st.experimental_data_editor')

#Drop box
option = st.selectbox('Select dataset',('Default dataset', 'Upload dataset'))
st.write('You selected:', option)

if option == 'Upload dataset':
    st.file_uploader("Select CSV file to upload", type=["csv"])

#Paths
file_path1 = pd.read_csv("NYC_most_pop.csv")
#file_path2 = st.file_uploader("Select CSV file to upload", type=["csv"])

#Progress bar
#progress_text = "Uploading in progress. Please wait."

#if 
#my_bar = st.progress(0, text=progress_text)

#for percent_complete in range(100):
    #time.sleep(0.1)
    #my_bar.progress(percent_complete + 1, text=progress_text)

#Editable dataset
df= load_data1(file_path1)
st.experimental_data_editor(df, num_rows="dynamic")
