import streamlit as st

st.title("Hello World!")
st.header("Example Header")
st.subheader("Example Sub-Header")
st.text("This is an example text.")

st.markdown(""" # h1 tag
## h2 tag
### h3 tag 
:moon: <br>
:sunglasses:""",True)

st.latex(r"""2x + \frac{2}{3}x^{\frac{3}{2}} + \frac{1}{x}\Biggr|_{1}^{9}""")

st.write("Vipul","Gaur","Learning Streamlit")