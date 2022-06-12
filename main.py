from optparse import Option
import streamlit as st
import numpy as np
import pandas as pd


st.title('streamlit_演習')


Option = st.selectbox(
    '君が好きなNo.は？',
    list(range(1, 100000))
)

'君が好きなNo.は', Option, 'だよね〜'