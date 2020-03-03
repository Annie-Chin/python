import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
city= st.selectbox('居住地', ['台北市'], ['台中市'], ['高雄市'])
st.write(f'你選擇了{city}!')
