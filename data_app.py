import streamlit as st
import pandas as pd
import time
from PIL import Image

# App config
st.set_page_config(layout="wide")

# Picture
image = Image.open('Streamlit.png')
st.image(image,width=200)

# Data cache
@st.cache_data()
def load_data1(file_path1):
    default_data = pd.read_csv(file_path1)
    return default_data

@st.cache_data()
def load_data2(file_path2):
    uploaded_data = pd.read_csv(file_path2)
    return uploaded_data

# Titles
st.title('Editable Dataframes')
st.markdown('Upload, Edit and Download datasets')

# Select box
option = st.selectbox('Select dataset', ('Default dataset', 'Upload dataset'))
st.write('You selected:', option)

# Uploading box
if option == 'Upload dataset':
    file_path2 = st.file_uploader("Select CSV file to upload", type=["csv"])
else:
    file_path2 = None

# Show/hide uploading box
if file_path2 is not None:
    data = load_data2(file_path2)
    st.experimental_data_editor(data, num_rows="dynamic")
    csv = data.to_csv(index=False) 
    
elif option == 'Default dataset':
    data = load_data1("NYC_most_pop.csv")
    st.experimental_data_editor(data, num_rows="dynamic")
    csv = data.to_csv(index=False)

# Download box
st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='Your_data.csv',
    mime='text/csv',
)
