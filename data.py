import streamlit as st
import pandas as pd
import numpy as np

a = list(range(1,10))

#l = a.res

st.write(type(a),a)

df = pd.DataFrame(np.array(a).reshape((3,3)),columns='C1 C2 C3'.split())

st.write(df)