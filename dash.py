import streamlit as st
import pandas as pd
import numpy as np

st.title('OT Project')

DATE_COLUMN = 'time_locs'
DATA_URL = ('5glhn8oo_clean_data.csv')



DATE_COLUMN_2 = 'time_locs'
DATA_URL_2 = ('5h167gur_clean_data.csv')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data


@st.cache
def load_data(nrows):
    data_2 = pd.read_csv(DATA_URL_2, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data_2.rename(lowercase, axis='columns', inplace=True)
    data_2[DATE_COLUMN_2] = pd.to_datetime(data_2[DATE_COLUMN_2])
    return data_2


data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text("Done! (using st.cache)")


data_load_state_2 = st.text('Loading data...')
data_2 = load_data(10000)
data_load_state_2.text("Done! (using st.cache)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data_2)

patient_1 = pd.read_csv('5glhn8oo_clean_data.csv')
patient_2 = pd.read_csv('5h167gur_clean_data.csv')
st.subheader('Satisfaction Patient 1')
satis = patient_1['Satisfaction'].value_counts()
st.bar_chart(satis)

st.subheader('Types of Activity for Patient 2')
activity = patient_2[['heavy_activity','mild_activity','moderate_activity']]
st.line_chart(activity)

code = '''@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data
'''
st.code(code,language= 'python')
st.caption('Above is Code that displays the raw dataset')

#pip3 install streamlit 
#pip3 install pipenv or Sudo -H pip install -U pipenv 
#pipenv shell
#pip install streamlit
