import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt

df = pd.DataFrame(np.random.randn(100,3),columns='A B C'.split())

chart = alt.Chart(df).mark_circle().encode(x='a',y='b')

st.altair_chart(chart)

fig, ax = plt.subplots()

ax.scatter(df['A'],df['B'])
st.pyplot(fig)

plt.scatter(df['A'],df['B'])
plt.title('Scatter Plot')
st.pyplot();

st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)
st.write(df)