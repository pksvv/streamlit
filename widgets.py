import streamlit as st

st.title('Widgets')

if st.button('Subscribe'):
    st.write("Like this video too.")


name = st.text_input("Name")
st.write(name)
