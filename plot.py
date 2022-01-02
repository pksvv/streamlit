import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import altair as alt

df = pd.DataFrame(np.random.randn(100,3),columns='A B C'.split())

city = pd.DataFrame({"awesome cities": ['Sonipat','Washington'],
                    "lat":[28.9931,47.7511],
                    "lon":[77.0151,120.7401]}
                    )

st.map(city)
st.map()

st.graphviz_chart("""
digraph{
    watch -> like
    like -> share
    share -> subscribe
    share -> watch
}
""")

chart = alt.Chart(df).mark_circle().encode(x='A',y='B')

st.altair_chart(chart, use_container_width=True)

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