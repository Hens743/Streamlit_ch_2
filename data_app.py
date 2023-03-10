import streamlit as st
import pandas as pd
import time

#App config
st.set_page_config(layout="centered")

#Data cache
@st.cache_data()
def load_data1(file_path1):
    default_data = pd.read_csv("NYC_most_pop.csv")
    return default_data

@st.cache_data()
def load_data2(file_path2):
    uploaded_data = pd.read_csv(file_path2)
    return uploaded_data

#Titles
st.header('Editable dataframes')
st.markdown ('Made with: Streamlit 1.19 - st.experimental_data_editor')

#Paths

#file_path2 = st.file_uploader("Select CSV file to upload", type=["csv"])
df= def load_data(url):
    df = pd.read_csv(url)  # 👈 Download the data
    return df

df = load_data("https://github.com/plotly/datasets/raw/master/uber-rides-data1.csv")
st.dataframe(df)

st.button("Rerun")
#Drop box
option = st.selectbox('Select dataset',('Default dataset', 'Upload dataset'))
st.write('You selected:', option)

if option == 'Default dataset':
    st.experimental_data_editor(file_path1, num_rows="dynamic")

if option == 'Upload dataset':
    st.file_uploader("Select CSV file to upload", type=["csv"])

#Progress bar
#progress_text = "Uploading in progress. Please wait."

#if 
#my_bar = st.progress(0, text=progress_text)

#for percent_complete in range(100):
    #time.sleep(0.1)
    #my_bar.progress(percent_complete + 1, text=progress_text)

#Editable dataset
#df= load_data1(file_path1)
#st.experimental_data_editor(df, num_rows="dynamic")
