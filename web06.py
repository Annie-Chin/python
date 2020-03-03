import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
coffee= st.slider('咖啡粉量', 10, 45, 20, 0.5)
water = 15*coffee
