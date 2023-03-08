import streamlit as st
import pandas as pd

#App config
st.set_page_config(layout="centered")

#Data cache
@st.cache_data()
def load_data(file_path1):
    df1 = pd.read_csv(file_path1)
    return df1

@st.cache_data()
def load_data(file_path2):
    df2 = pd.read_csv(file_path2)
    return df2

#Building
st.header('Dataframes editor app')
st.markdown ('Streamlit 1.19 - st.experimental_data_editor')

option = st.selectbox('Select dataset',('Default dataset', 'Upload dataset'))
st.write('You selected:', option)

#Drop box
if st.selectbox == ('Default dataset'):
    st.file_uploader(label_visibility)
    label_visibility=st.session_state.visibility, disabled=st.session_state.disabled
else
   st.file_uploader("Select CSV file to upload", type=["csv"])
