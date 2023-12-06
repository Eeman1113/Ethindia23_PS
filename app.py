import streamlit as st
import pandas as pd
st.markdown("<h1 style='text-align: center; '>CookEthNotMeth</h1>", unsafe_allow_html=True)
df = pd.read_csv('./data/eth23.csv')
count = 1

for i in df['Summary']:
    st.markdown('___')
    st.write(count,".")
    st.write(i)
    count+=1
st.balloons()