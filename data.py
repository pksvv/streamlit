import streamlit as st
import pandas as pd
import numpy as np
import time

a = list(range(1,10))

#l = a.res

st.write(type(a),a)

df = pd.DataFrame(np.array(a).reshape((3,3)),columns='C1 C2 C3'.split())

st.write(df)

@st.cache
def return_time(a):
    time.sleep(5)
    return time.time()

if st.checkbox("1"):
    st.write(return_time(1))

if st.checkbox("2"):
    st.write(return_time(2))