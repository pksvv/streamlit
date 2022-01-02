import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(100,3),columns='A B C'.split())