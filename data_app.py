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

#option = st.selectbox('Select dataset',('Default dataset', 'Upload dataset'))
#st.write('You selected:', option)

#Drop box
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

if st.selectbox == ('Default dataset'):
    #st.file_uploader(disabled)
    label_visibility=st.session_state.visibility, disabled=st.session_state.disabled

#if upload:
   
#####
file_path = st.file_uploader("Select CSV file to upload", type=["csv"])

if file_path:
    dataset = load_data(file_path)
    top_menu = st.columns(3)
    with top_menu[0]:
        default = st.radio("Default dataset", options=["Yes", "No"], horizontal=1, index=1)
    if default == "Yes":
        with top_menu[1]:
            sort_field = st.selectbox("Sort By", options=dataset.columns)
        with top_menu[2]:
            sort_direction = st.radio("Direction", options=["⬆️", "⬇️"], horizontal=True)
        dataset = dataset.sort_values(by=sort_field, ascending=sort_direction == "⬆️", ignore_index=True)
        
#Editable dataset
edited_df = st.experimental_data_editor(df, num_rows="dynamic")

favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
st.markdown(f"Your favorite command is **{favorite_command}** 🎈")
