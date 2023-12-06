import streamlit as st
import pandas as pd
st.markdown("<h1 style='text-align: center; '>CookEthNotMeth</h1>", unsafe_allow_html=True)
df = pd.read_csv('./data/eth23.csv')
count = 1

for i in range(0,len(df['Summary'])):
    st.markdown('___')
    st.write(count,".")
    st.write(df['Summary'][i])
    st.markdown(f"<details><summary>For More Info About Me Click Here</summary>{df['Problem Statement'][i]}</details>",unsafe_allow_html=True)
    count+=1
st.balloons()
