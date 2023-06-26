import streamlit as st
import pickle
import pandas as pd
import sklearn
import numpy as np

st.header('Are you sure want to leave this page?')


url = 'https://stackoverflow.com'
url1 = 'https://vitascan-smart-o-thon-lung-cancer-webapp-htnx26.streamlit.app/'
st.markdown(f'''
<a href={url}><button style="background-color:White;  height: 2em; width: 18em; font-size:30px;">Yes</button></a>
''',
unsafe_allow_html=True)


st.markdown(f'''
<a href={url1}><button style="background-color:White;height: 2em; font-size:30px; width: 18em">No</button></a>
''',
unsafe_allow_html=True)
