# Import libraries
import streamlit as st
import pandas as pd

#Utils
import base64
import time

from streamlit.config import on_config_parsed
timestr = time.strftime("%Y%m%d-%H%M%S")
# Fxn to download
def csv_downloader(data): 
    csvfile = data.to_csv() 
    b64 = base64.b64encode(csvfile.encode()).decode()
    new_filename = "new_csv_file_{}_.csv".format(timestr)
    st.markdown("#### Download File ###")
    href = f'<a href="data:file/csv;base64,{b64}" download="{new_filename}">Click Here!!</a>'
    st.markdown(href,unsafe_allow_html=True) 

# Title of App
st.title("Data Preprocessing App")
# Upload dataset 
df1 = st.file_uploader(label = "upload Dataset 1 ",type = "CSV")
df2 = st.file_uploader(label = "upload Dataset 2 ",type = "CSV")
if df1 is not None: 
    df1 = pd.read_csv(df1)
    st.write(df1)
if df2 is not None: 
    df2 = pd.read_csv(df2)
    st.write(df2)
    
# Operations
Operation = st.selectbox("Operation",["None","Merge","Concat","Compare"])
if Operation == "None": 
    st.write("Please select your operation")

# # Merge method
#output1 = pd.merge(df1,df2)
if Operation == "Merge": 
    
    Columns=st.multiselect("Please select column",df1.columns.unique())
    how = st.selectbox("how",["inner","left","right","outer"])

    for i in Columns: 
        output1 = pd.merge(df1,df2,on=i,how=how)
        st.write(output1)   
        csv_downloader(output1)

# Concat method
output2 = pd.concat([df1,df2],ignore_index=True)
if Operation == "Concat": 
    st.write(output2)
    csv_downloader(output2)

#Compare Method: Align the differences on rows
output3 = df1.compare(df2,align_axis=0) 
if Operation == "Compare": 
    st.write(output3)
    csv_downloader(output3)
    
# Create a simple buttuon 
# st.button("Cancel")
st.text("Thank you!!!") 


