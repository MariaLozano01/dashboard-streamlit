import streamlit as st
import pandas as pd
import numpy as np

st.title('OT Project')

patient_data_1 = pd.read_csv('5glhn8oo_clean_data.csv')

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(patient_data_1)

################################## PATIENT 2 ##################################

patient_data_2 = pd.read_csv('5h167gur_clean_data.csv')

if st.checkbox('Show Raw Data 2'):
    st.subheader('Raw Data 2')
    st.write(patient_data_2)


st.subheader('Satisfaction Patient 1')
satis = patient_data_1['Satisfaction'].value_counts()
st.bar_chart(satis)

st.subheader('Types of Activity for Patient 2')
activity = patient_data_2[['heavy_activity','mild_activity','moderate_activity']].value_counts()
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


#sudo apt-get update && sudo apt-get upgrade -->to update and upgrade terminal at the same time
#sudo apt install python3-pip
#pip3 install streamlit 
#pip3 install pipenv or Sudo -H pip install -U pipenv 
#pipenv shell
#pip install streamlit

#sudo apt-get update
#sudo apt install python3-pip
#pip3 install pandas 
#sudo -h pip install -u pipenv 
#pip3 install streamlit 


#sudo apt install python3-venv


############################################
#On Azure --> My Mac Terminal 
#sudo apt-get update
#sudo apt install python3-pip
# pip3 install streamlit
#nano ~.bashrc
#source ~.bashrc
#~$ streamlit
#$ pip install pandas
#pip3 install jinja2
#pip3 install jinja2 --upgrade
#ls into repo 
#streamlit run dash.py
#copy external URL to see data visuals 
